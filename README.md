# Feira Livre
## API REST, testes unitários, importação de arquivo CSV

* Ambiente: .venv
* Projeto: fairfree
* App: api
* Model: Fair
* Fields: id, long, lat, setcens, areap, coddist, distrito, codsubpref, subprefe, regiao5, regiao8, nome, registro, logradouro, numero, bairro, referencia

## Instalação

1. Faça o checkout do projeto:

```bash
$ git clone https://github.com/brunaangelino/fairfree.git
```

2. Crie um ambiente virtualizado com [virtualenv]() e ative-o:

```bash
$ cd fairfree
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Executando o último comando, deve aparecer dessa forma:

```bash
(.venv)$
```

Isso significa que o ambiente foi ativado com sucesso. Agora vamos instalar as dependências executando o arquivo `requirements.txt`:
```bash
(.venv)$ pip install -r requirements.txt
```

ou pode instalar as dependências uma por uma, assim:

```bash
(.venv)$ pip install django
(.venv)$ pip install djangorestframework
(.venv)$ pip install django-filter
(.venv)$ pip install mixer
(.venv)$ pip install lxml
```

após instalar todas as dependências:

```bash
(.venv)$ pip freeze
```

deverá conter esses pacotes:

```bash
Django==2.0.5
django-filter==1.1.0
djangorestframework==3.8.2
Faker==0.8.8
lxml==4.2.1
mixer==6.0.1
python-dateutil==2.7.3
pytz==2018.4
six==1.11.0
text-unidecode==1.2
```

3. Rode o comando abaixo para o Django criar o banco local e executar as migrações que criamos:

```bash
(.venv)$ python manage.py migrate
```

4. Agora rode o projeto com o servidor embarcado:

```bash
(.venv)$ python manage.py runserver
```

5. Acesse o sistema em `http://localhost:8000`.

6. Para executar os testes unitários:

```bash
(.venv)$ python manage.py test
```

7. Para executar o script para importar o arquivo `DEINFO_AB_FEIRASLIVRES_2014.csv`:

```bash
(.venv)$ python manage.py import_archive_csv_fair DEINFO_AB_FEIRASLIVRES_2014.csv
```
