from database import db, Usuario, Anuncio

db.connect() #Conecta o banco de dados

db.create_tables([Usuario, Anuncio]) #Cria tabelas com base em uma lista de tabelas

# ---- Criando usuário:
# usuario = Usuario.create(nome="Tiago", email="tiago@gmail.com", senha="minhasenha123")

#print("Novo usuário: ", usuario.id, usuario.nome, usuario.email)

# ---------- Selecionando todos os usuários e adicionando em uma lista
# lista_usuarios = Usuario.select()
# print("Lista de Usuários:")
# for x in lista_usuarios:
#     print("Usuário: ", x.id, " - Nome: ", x.nome, " - E-mail: ", x.email)

# -------- Alterando dados de um usuário ja criado:
# usuario_1 = Usuario.get(Usuario.email == "joao@gmail.com")
# usuario_1.nome = "João vieira"
# usuario_1.save()
#print(usuario_1.nome)

# ----------- Testando criação de usuário com e-mail ja cadastrado através de try e except
# try:
#     usuario = Usuario.create(nome="Tiago", email="tiago@gmail.com", senha="minhasenha123")
# except:
#     print("E-mail ja existe no banco de dados!")


# ----------- Deletando usuário cadastrado no sistema e buscando para ver se o mesmo ainda existe

# usuario_1 = Usuario.get(Usuario.email == "tiago@gmail.com")
# usuario_1.delete_instance()

# try:
#     busca = Usuario.get(Usuario.email == "tiago@gmail.com")
# except:
#     print("Usuário deletado!")


# anuncio = Anuncio.create(
#     usuario = joao,
#     titulo = "Video de banco de dados",
#     descricao = "A descrição pode ser qualquer coisa",
#     valor = 500.0
# )

# anuncio = Anuncio.create(
#     usuario = joao,
#     titulo = "Curso de C#",
#     descricao = "A descrição pode ser qualquer coisa referente a c#",
#     valor = 500.0
# )

# anuncio = Anuncio.create(
#     usuario = adriel,
#     titulo = "Curso de Java",
#     descricao = "A descrição pode ser qualquer coisa referente a Java",
#     valor = 500.0
# )

# ----------- Filtra todos os anuncios relacionados a joao
# joao = Usuario.get(Usuario.email == "joao@gmail.com")

# anuncios_joao = Anuncio.select().join(Usuario).where(Usuario.email == joao.email)

# print("Anuncios João:")
# for a in anuncios_joao:
#     print(" - ", a.id, a.titulo, a.valor)

Anuncio.delete().execute()

print("Quantidade de anuncio: ", Anuncio.select().count())