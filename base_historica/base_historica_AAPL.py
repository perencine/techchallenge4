"""
Download de base de ações da Apple, do início de 2017 ao fim de 2023
"""

import yfinance as yf

acao = "AAPL"
dt_inicio = "2017-01-01"
dt_fim = "2024-01-01"

df_acao = yf.download(acao, start=dt_inicio, end=dt_fim)
df_acao = df_acao[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
df_acao.reset_index(inplace=True)
df_acao.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

df_acao.to_csv(f"{acao}_7_years_data.csv", index=False)
