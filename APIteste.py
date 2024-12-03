from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
import numpy as np
import pandas as pd
import joblib
import torch.nn as nn

# Carregar o scaler e os hiperparâmetros
scaler = joblib.load('scaler.pkl')
modelo_hiperp = torch.load('modelo_aapl_lstm.pth', map_location=torch.device('cpu'))
hiperp = modelo_hiperp['hyperparameters']
modelo = modelo_hiperp['model_state_dict']
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Definição da classe LSTM
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm1 = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc1 = nn.Linear(hidden_size, output_size)
        self.lstm2 = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        
        out, _ = self.lstm1(x, (h0, c0))
        out = self.fc1(out[:, -1, :])
        out, _ = self.lstm2(x, (h0, c0))
        out = self.fc2(out[:, -1, :])
        return out

app = FastAPI()

class StockInput(BaseModel):
    Date: list[str] = Field(..., min_items=20, max_items=20)
    Open: list[float] = Field(..., min_items=20, max_items=20)
    High: list[float] = Field(..., min_items=20, max_items=20)
    Low: list[float] = Field(..., min_items=20, max_items=20)
    Volume: list[int] = Field(..., min_items=20, max_items=20)

@app.post("/predict/")
def predict_stock(input_data: StockInput):
    try:
        df = pd.DataFrame({
            'Date': pd.to_datetime(input_data.Date),
            'Open': input_data.Open,
            'High': input_data.High,
            'Low': input_data.Low,
            'Volume': input_data.Volume
        })
        df['Weekday'] = df['Date'].dt.weekday
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['day_sin'] = np.sin(2 * np.pi * df['Date'].dt.dayofyear / 365)
        df['day_cos'] = np.cos(2 * np.pi * df['Date'].dt.dayofyear / 365)
        df['Close'] = 0  # Placeholder para normalização


        cols_norm = ['Open', 'High', 'Low', 'Close', 'Volume', 'Weekday', 'Month', 'Year']
        df_norm = df[cols_norm + ['day_sin', 'day_cos']].copy()
        df_norm[cols_norm] = scaler.transform(df_norm[cols_norm])
        df_norm = df_norm.drop('Close', axis=1)  # Remover 'Close' para a predição

        model = LSTM(hiperp['input_size'], hiperp['hidden_size'], hiperp['num_layers'], hiperp['output_size']).to(device)
        model.load_state_dict(modelo)
        model.eval()

        X = torch.tensor(df_norm.values, dtype=torch.float32).unsqueeze(0).to(device)
        with torch.no_grad():
            predicted_close_normalized = model(X).item()

        # Desnormalizar o valor de 'Close'
        close_index = cols_norm.index('Close')
        min_close, max_close = scaler.data_min_[close_index], scaler.data_max_[close_index]
        predicted_close = predicted_close_normalized * (max_close - min_close) + min_close

        return {"predicted_close": predicted_close}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
