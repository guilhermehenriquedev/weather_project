
# Weather Forecast

API de consulta de previsão de tempo dos proximos 5 dias


## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:guilhermehenriquedev/weather_project.git
```

Ative o ambiente virtual

```bash
  python3 -m venv venv
  source venv/bin/activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```


Para rodar esse projeto, você vai precisar gerar uma APIKEY no site https://openweathermap.org/ e adcionar no seu .env

`OPENWEATHERMAP_API_KEY`=SUA_API_KEY

Aplique as migrações

```bash
  cd weather_app
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Inicie o Servidor
```bash
    python3 manage.py runserver
```


## Documentação da API

#### Retorna histórico de buscas

```http
  GET /api/weather_history
```

#### Envia para o banco de dados o historico de busca

```http
  POST /api/weather_history
```

| raw data   | Tipo       | 
| :---------- | :--------- | 
| `{"cidade": "string","data": {json}}`      | `json` |


#### Retorna historicos de busca de uma cidade

```http
  GET /api/weather_history?search=teresina
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `search`      | `string` | **Obrigatório**. O nome da cidade que você quer |


#### Retorna dados de previsão de tempo dos próximos 5 dias de uma determinada cidade

```http
  GET /api/weather_forecast/get/?city=teresina
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `city`      | `string` | **Obrigatório**. O nome da cidade que você quer |





## Logs
A aplicação conta com um sistema de logs padrão do Django, para localizar entre na pasta
```bash
    cd weather_project/weather_app/logs
    vim application.log
```
## Stack utilizada

**Back-end:** Python, Django \
**Banco de dados:** Sqlite3

