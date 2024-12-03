# API Preço Ação Apple - Tech Challenge 4

#### Criadores: Vitor Mamede | Vitor Perencine
#### Grupo 86

<br/>

## 1. Objetivo

Este projeto foi desenvolvido para que usuários pudessem consultar via API o valor da previsão de fechamento da ação AAPL (Apple), em determinado dia. A previsão dos valores é realizada por um modelo de Deep Learning, treinado com a base histórica de 7 anos da ação, e é realizada a partir dos parâmetros que o usuário fornece no ato da requisição.

<br/>

## 2. Descrição da API:

Esta API foi desenvolvida em Python, utilizando o framework FastAPI.

O modelo de Deep Learning utilizado é um LSTM (Long Short-Term Memory), reconhecido por sua capacidade em lidar com valores contínuos de séries temporais. Ele foi treinado com dados históricos das ações da Apple (AAPL), abrangendo o período de janeiro de 2017 a outubro de 2024, obtidos por meio da biblioteca `yfinance` do Python.

Para obter a previsão do preço de fechamento da ação, é necessário fornecer os seguintes parâmetros: Data, Valor de Abertura, Valor Máximo, Valor Mínimo e Volume Operado. A formatação correta desses dados está detalhada no tópico abaixo.

**Repositório da API no github**: https://github.com/perencine/techchallenge4

<br/>

## 3. Endpoint disponibilizado

Previsão de fechamento: /predict/

Devem ser feitas requisições GET, passando-se os parâmetros abaixo em um dicionário:

| Parâmetro | Tipo | Descrição |
| --------- | ---- | --------- |
| `date` | list | Data(s) de requisição no formato yyyy-mm-dd |
| `open` | list | Valor(es) de abertura da ação, no formato ###.## |
| `high` | list | Valor(es) máximo(s) da ação, no formato ###.## |
| `low` | list | Valor(es) mínimo(s) da ação, no formato ###.## |
| `volume` | list | Volume(s) operado(s), em números inteiros |

Segue exemplo de envio de dados à API:

![image](https://github.com/user-attachments/assets/67e91f8c-7eaf-4024-98b4-dd014058d3fa)


O retorno da API é um dicionário no modelo:
```python
{'predicted_close': 'valor'}
```

Conforme exemplo:

![image](https://github.com/user-attachments/assets/eb88eefd-e35e-4aea-ad5c-9bf24221dbfb)

<br/>

## 4. Arquitetura do projeto

<br/>

![{6762A4C6-AF58-475F-9739-E91130430E3A}](https://github.com/user-attachments/assets/59f62970-ca12-49ff-9401-c2681e47e79f)

<br/>

## 5. Cenário de Utilização


### Introdução:

Um consumidor de informações de ações da Apple consulta tais dados diariamente na internet, avaliando quando deve comprar ou vender ações a partir de dados gerais da ação (valor de abertura, máxima do dia, mínima, etc)

### Problema

O usuário se sente inseguro sobre qual decisão tomar - comprar, vender ou manter suas posições, dado a variabilidade do preço da ação.

### Solução:

O usuário utiliza a API para predizer o valor de fechamento da ação, o que o auxilia na tomada de decisão. Para tal, ele deve consultar o endpoint `/predict`, passando as informações requeridas, a fim de se obter a previsão.

### Benefícios:

Essa arquitetura proporciona uma maneira eficiente e segura de fornecer previsões de fechamento da ação AAPL. O usuário, munido desta previsão e das demais informações que já possuia, toma decisões mais seguras e baseadas em dados.

<br/>
<br/>
<br/>
<br/>

Licença

MIT Licence.
