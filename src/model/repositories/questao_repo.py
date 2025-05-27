from src.model.entities.questao import Questao
from src.model.entities.alternativa import Alternativa
from src.model.settings.connection import DBConnectionHandler
from sqlalchemy.orm import joinedload


class QuestaoRepository:

    @classmethod

    def insert_question(self, new_question:Questao)->None:

        try:

            with DBConnectionHandler() as database:

                database.session.add(new_question)
                database.session.commit()

        except Exception as exception:

            database.session.rollback()
            raise exception
        
    @classmethod

    def get_all(self):

        try:
            with DBConnectionHandler() as database:
                questions = (
                    database.session
                    .query(Questao)
                    .options(joinedload(Questao.alternativas))  # Aqui carrega as alternativas junto
                    .all()
                )
                return questions
        except Exception as e:
            raise e
        
    
    @classmethod

    def get_question_id_by_enunciado(self, enunciado):

        try:
            with DBConnectionHandler() as database:

                questao = database.session.query(Questao).filter(Questao.enunciado==enunciado).one()

                return questao.id
            
        except Exception as exception:

            database.session.rollback()
            raise exception