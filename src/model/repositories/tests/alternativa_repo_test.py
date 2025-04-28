from src.model.entities.alternativa import Alternativa
from src.model.entities.questao import Questao
from src.model.repositories.alternativa_repo import AlternativaRepository
from src.model.repositories.questao_repo import QuestaoRepository
from src.model.settings.connection import DBConnectionHandler
from sqlalchemy import text
import pytest



db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_alternative():

    mock_enunciado_questao = "Qual a capital da Alemanha?"
    mock_dica = "Participante de La Casa de Papel"
    mock_materia = "GEOGRAFIA"
    new_question = Questao(enunciado = mock_enunciado_questao, dica = mock_dica,  materia=mock_materia)
    QuestaoRepository.insert_question(new_question=new_question)

    mock_id_questao = QuestaoRepository.get_question_id_by_enunciado(mock_enunciado_questao)

    mock_enunciado_alternativa = "Moskou"
    mock_verify = 0

    new_alternativa = Alternativa(q_id = mock_id_questao, enunciado = mock_enunciado_alternativa, verify = mock_verify)
    AlternativaRepository.insert_alternative(new_alternative=new_alternativa)


    sql = '''
SELECT * FROM alternativa
WHERE q_id = "{}"
and enunciado = "{}"
and verify = "{}"
'''.format(mock_id_questao, mock_enunciado_alternativa, mock_verify)
    
    response = connection.execute(text(sql))

    registry = response.fetchall()[0]

    assert registry.enunciado == mock_enunciado_alternativa
    assert registry.verify == mock_verify
    assert registry.q_id == mock_id_questao


    sql_delete = '''
DELETE FROM questao 
WHERE enunciado = "{}"
and dica = "{}"
and id = "{}"
'''.format(mock_enunciado_questao, mock_dica, mock_id_questao)
    
    connection.execute(text(sql_delete))
    connection.commit()

    connection.close()
    