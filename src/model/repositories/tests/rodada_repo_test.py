from src.model.entities.rodada import Rodada
from src.model.entities.usuario import Usuario
from src.model.repositories.usuario_repo import UserRepository
from src.model.repositories.rodada_repo import RodadaRepository
from src.model.settings.connection import DBConnectionHandler
import bcrypt
import pytest
from sqlalchemy import text
from datetime import date



db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_rodada():

    mockname = "teste"
    mockemail = "teste@gmail.com"
    mockpassword = bcrypt.hashpw("123456".encode(), bcrypt.gensalt())
    mocktype = 0

    new_user = Usuario(email = mockemail, nome = mockname, senha = mockpassword, type = mocktype)

    UserRepository.insert_user(new_user_registry=new_user)

    mock_user_id = UserRepository.get_user_by_email(mockemail).id
    mock_pontuacao = 100
    mock_data = date(2025,4,28)

    new_rodada = Rodada(pontuacao = mock_pontuacao, data = mock_data, id_usuario=mock_user_id)

    RodadaRepository.insert_round(new_round=new_rodada)

    sql = '''
SELECT * FROM rodada
WHERE id_usuario = "{}"
and pontuacao = "{}"
and data = "{}"
'''.format(mock_user_id,mock_pontuacao,mock_data.strftime('%Y-%m-%d'))
    
    response = connection.execute(text(sql))

    registry = response.fetchall()[0]


    assert registry.id_usuario == mock_user_id
    assert registry.pontuacao == mock_pontuacao
    assert registry.data == mock_data


    sql_delete = '''
DELETE FROM usuario
WHERE nome = "{}"
and email = "{}"
and type = "{}"
'''.format(mockname, mockemail, mocktype)
    
    connection.execute(text(sql_delete))
    connection.commit()

    connection.close()
