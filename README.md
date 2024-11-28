# Projeto API Preço Ação Apple - Tech Challenge 4

### Criadores: Vitor Mamede | Vitor Perencine
### Grupo 86

<br/>

## Objetivo

Este projeto foi desenvolvido para que usuários pudessem consultar via API o valor da previsão de fechamento da ação AAPL, da Apple, em determinado dia. Para tal, deve-se passar os parâmetros: Data, Valor de Abertura, Valor Máximo, Valor Mínimo e Volume Operado, e sua formatação será devidamente explicada nos tópicos abaixo.

Para que a API pudesse retornar a previsão de fechamento da ação, foi utilizado um modelo de Deep Learning, treinado com a base histórica de 7 anos da ação. A API fornece os parâmetros para o modelo, que devolve a previsão de fechamento do valor no dia fornecido.

<br/>

## Descrição da API:

Esta API foi desenvolvida em Python, utilizando o framework FastAPI.

O modelo escolhido e treinado foi o LSTM, por sua capacidade em lidar com valores contínuos de séries temporais. Ele foi treinado com dados de jan/2017 a dez/2023, que foram obtidos através da biblioteca `yfinance`do python.

<br/>

## Repositório da API no github

https://github.com/perencine/techchallenge4

<br/>

## Endpoints disponibilizados (editar se preciso)
Devem ser chamados com requisições GET, a fim de se obter os dados desejados. Segue a relação de dados desejados e endpoints:

Auth : /token/

Previsão de fechamento: /forecast/

<br/>

## Autenticação (editar)

Antes de utilizar a API, deve-se chamar o endpoint /token com requisição POST para se obter um token JWT, enviando os parâmetros "username" e "password". Segue exemplo de request em Bash, considerando que se deve substituir SEU_USER pelo usuário e SUA_SENHA pela senha:

 (inserir exemplo e remover o abaixo)
 
![image](https://github.com/mamedevitor/techchallenge/assets/55901404/ce89c34b-30da-4014-980d-f0c4bc4d4f18)

Modelo da response:

 (inserir exemplo e remover o abaixo)

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/1ae943b6-6dbc-47cd-a10f-7ef99e11dd01)

## Requisição (editar)

A relação abaixo detalha os parâmetros que devem ser passados à API, bem como detalhes de cada um:

| Parâmetro | Tipo | Descrição |
| --------- | ---- | --------- |
| `date` | String | Data da requisição no formato yyyy-mm-dd |
| `open` | String | Valor de abertura da ação, no formato ###.## |
| `high` | String | Valor máximo da ação, no formato ###.## |
| `low` | String | Valor mínimo da ação, no formato ###.## |
| `volume` | String | Volume operado, em números inteiros |

Segue exemplo de envio de dados à API, em bash:

(inserir exmeplo)

O retorno da API é um dicionário no modelo:
```python
{'close': 'valor'}
```
<br/>

# Processo de deploy da API (editar)

## Deploy no desktop

Após a replicação do repositório no ambiente de execução, basta seguir os passos listados abaixo:

#### Crie um ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
#### Rodando o projeto

```bash
uvicorn app.main:app --reload
```
 
## Deploy no Heroku

#### 1. Criar repositório no github:
```bash
git init
git add .
git commit -m "Initial commit"
```

#### 2. Crie um arquivo Procfile na raiz do projeto e dentro dele o seguinte código:
```bash
web: uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
```

#### 3. Crie um novo aplicativo no Heroku:
```bash
heroku create vitibrasil-api
```
#### 4. Faça o deploy para o Heroku:
```bash
git push heroku master
```
#### 5. Escale a aplicação:
```bash
heroku ps:scale web=1
```

#### 6. Acesse sua aplicação:
Heroku fornecerá um link para a aplicação. Acesse o link para ver sua API em funcionamento na nuvem.
https://api-tech-challenge-fiap-ba4acd78ab5d.herokuapp.com/docs

# Arquitetura do projeto
<br/>

![apitechchallenge drawio](https://github.com/mamedevitor/techchallenge/assets/83721127/2494997e-96d8-41e2-82ab-7816b7c9cb8f)

# Cenário de Utilização (editar)


### Objetivo: 
Imaginando que o usuário será um vinicultor afim de analisar a produtividade de diferentes variedades de uvas ao longo dos anos para tomar decisões informadas sobre plantio e produção.

### Processo:

Login: Vinicultor faz login e obtém um token JWT.

### Consulta de Dados:
1. Vinicultor faz uma requisição para o endpoint /producao/ para obter dados históricos de produção.
2. Utiliza filtros para analisar a produtividade de um determinado período.

3. Análise e Decisão:
Com base nos dados recebidos, vinicultor pode decidir ajustar o cultivo de certas variedades de uvas, planejar a produção de vinho, ou fazer previsões para a próxima safra.
Essa arquitetura proporciona uma maneira eficiente e segura de fornecer acesso a dados valiosos, suportando a tomada de decisões baseadas em dados para vinicultores e outros usuários interessados.


<br/>
<br/>
<br/>
<br/>

Licença

MIT Licence.
