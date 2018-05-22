 ## Step-0 Projeto inicial
 
 Abra o arquivo `settings.py` e em `INSTALLED_APPS` acrescente
 
 ```python
 INSTALLED_APPS = (
 	...
     'rest_framework',
     'api',
 )
 ```
 
 ## Step-1 Models
 
 ### `models.py`: Criando o modelo `Fair`
 
 ```python
 class Fair(models.Model):
     id = models.CharField(max_length=8, verbose_name='Identificação')
     long = models.CharField(max_length=10, verbose_name='Longitude')
     lat = models.CharField(max_length=10, verbose_name='Latitude')
     setcens = models.CharField(max_length=15, verbose_name='Setor censitário')
     areap = models.CharField(max_length=13, verbose_name='Área de ponderação')
     coddist = models.CharField(max_length=9, verbose_name='Código do distrito')
     distrito = models.CharField(max_length=18, verbose_name='Distrito municipal')
     codsubpref = models.CharField(max_length=2, verbose_name='Código da subprefeitura')
     subpref = models.CharField(max_length=25, verbose_name='Subprefeitura')
     regiao5 = models.CharField(max_length=6, verbose_name='Região conforme divisão do município em 5 áreas')
     regiao8 = models.CharField(max_length=7, verbose_name='Região conforme divisão do município em 8 áreas')
     nome = models.CharField(max_length=30, verbose_name='Nome da feira livre')
     registro = models.CharField(max_length=6, primary_key=True, verbose_name='Registro da feira livre')
     logadouro = models.CharField(max_length=34, verbose_name='Logradouro')
     numero = models.CharField(max_length=5, verbose_name='Número')
     bairro = models.CharField(max_length=20, verbose_name='Bairro')
     referencia = models.CharField(max_length=24, verbose_name='Ponto de referência')
 
     def __str__(self):
         return self.nome
 ```
 
 ### Fazendo a migração
 
 ```bash
 $ cd ..
 $ python manage.py makemigrations api
 $ python manage.py migrate
 ```
 
 ## Step-2 ModelSerializer
 
 ### `serializers.py`: Criando `FairSerializer`
 
Precisamos proporcionar uma forma de serialização e desserialização das instâncias de `fair` em uma representação JSON.
 
 ```bash
 $ cd api
 $ mkdir rest
 $ cd rest
 $ echo > serializers.py
 ```
 
 Edite
 
 ```python
 # -*- coding: UTF-8 -*-
 from rest_framework.serializers import ModelSerializer, CharField
 
 from api.models import Fair
 
 
 class FairSerializer(ModelSerializer):
     class Meta:
         model = Fair
         fields = '__all__'
 
 
 class FairListSerializer(FairSerializer):
     pass
 
 
 class FairDetailSerializer(FairSerializer):
     registro = CharField(max_length=6, read_only=True)
 ```
 
 Normalmente a primeira parte da classe define os campos que serão serializados. Neste caso, por ser serialização de uma model eu vou utilizar todos os campos, sendo assim utilizo fields = '__all__'.
 
 Uma classe de serialização é similar a uma classe `Form` do Django, e inclui validações similares para os campos, tais como `required`, `max_length`,  `default` e `read_only`.
 
 Criei três serializers, sendo FairSerializer o comum, com informação da model e dos campos visiveis, o FairListSerializer que não é preciso implentar nada pois precisamos do mesmo comportamento do FairSerializer e o FairDetailSerializer que foi necessário colocar o campo registro como `read_only` pois ele não poderá sofrer alterações na atualização do objeto Fair.
 
 É importante lembrar que as classes `ModelSerializer` não faz nenhuma mágica, são simplesmente um atalho para a criação das classes de serialização:
 * Os campos são definidos automaticamente.
 * Os métodos `create()` e `update()` são implementados por padrão de uma forma simplificada.
