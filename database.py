from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True) # só aceitará e-mails únicos
    senha = CharField()

    class Meta: #comando obrigatório para o peewee entender a qual banco essa classe está se referindo
        database = db # comando básico para informar o banco para a variável database, no caso o db

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios') #Campo de chave estrangeira, passando como parâmetro a tabela na qual será referenciada e um nome de referencia para o campo 
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()

    class Meta:
        database = db