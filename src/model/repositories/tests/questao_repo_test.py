from src.model.entities.questao import Questao
from src.model.entities.alternativa import Alternativa
from src.model.repositories.questao_repo import QuestaoRepository
from src.model.settings.connection import DBConnectionHandler
import pytest
from sqlalchemy import text


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_question():

    mock_enunciado = "Qual a capital da Alemanha?"
    mock_dica = "Participante de La Casa de Papel"
    mock_materia = "GEOGRAFIA"
    new_question = Questao(enunciado = mock_enunciado, dica = mock_dica, materia = mock_materia)
    QuestaoRepository.insert_question(new_question=new_question)

    sql = '''
SELECT * FROM questao
WHERE enunciado = "{}"
and dica = "{}"
'''.format(mock_enunciado, mock_dica)
    
    response = connection.execute(text(sql))

    registry = response.fetchall()[0]

    assert registry.enunciado == mock_enunciado
    assert registry.dica == mock_dica

    mock_question_id = QuestaoRepository.get_question_id_by_enunciado(mock_enunciado)

    sql_delete = '''
DELETE FROM questao 
WHERE enunciado = "{}"
and dica = "{}"
and id = "{}"
'''.format(mock_enunciado, mock_dica, mock_question_id)
    
    connection.execute(text(sql_delete))
    connection.commit()

    connection.close()
    
    