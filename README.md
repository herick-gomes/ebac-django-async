# Django Async Views - EBAC Modulo 11

Projeto Django com view assincrona e contador de tempo.

## Executar

python -m pip install -r requirements.txt
python manage.py migrate
python -m uvicorn config.asgi:application --reload

## Endpoint

GET /contador/

## Testes

python manage.py test
