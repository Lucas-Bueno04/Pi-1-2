import pytest
from sqlalchemy import text
from src.model.repositories.usuario_repo import UserRepository
from src.model.entities.usuario import Usuario
from src.model.entities.rodada import Rodada
import bcrypt
from src.model.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_user():

    mockname = "teste"
    mockemail = "teste@gmail.com"
    mockpassword = bcrypt.hashpw("123456".encode(), bcrypt.gensalt())
    mocktype = 0

    new_user = Usuario(email = mockemail, nome = mockname, senha = mockpassword, type = mocktype)

    UserRepository.insert_user(new_user_registry=new_user)

    sql = '''
SELECT * FROM usuario
WHERE nome = "{}"
and email = "{}"
'''.format(mockname, mockemail)

    response = connection.execute(text(sql))

    registry = response.fetchall()[0]

    
    assert registry.nome == mockname
    assert registry.email == mockemail
    assert registry.type == mocktype
    assert bcrypt.checkpw('123456'.encode(), registry.senha)

    sql_delete = '''
DELETE FROM usuario
WHERE nome = "{}"
and email = "{}"
and type = "{}"
'''.format(mockname, mockemail, mocktype)
    
    connection.execute(text(sql_delete))
    connection.commit()

    connection.close()
