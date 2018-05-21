# Feira Livre - API REST, testes unitários, importação de arquivo CSV

Então para criar a API, no meu caso, eu usei:

* Ambiente: .venv
* Projeto: fairfree
* App: api
* Model: Fair
* Fields: id, long, lat, setcens, areap, coddist, distrito, codsubpref, subprefe, regiao5, regiao8, nome, registro, logradouro, numero, bairro, referencia

## Clonando o projeto

```bash
$ git clone https://github.com/brunaangelino/fairfree.git
$ cd fairfree
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python contrib/env_gen.py
$ python manage.py migrate
```

Veja o meu requirements.txt

```bash
Django==2.0.5
django-filter==1.1.0
djangorestframework==3.8.2
lxml==4.2.1
mixer==6.0.1
```
