from src.model.entities.alternativa import Alternativa
from src.model.settings.connection import DBConnectionHandler



class AlternativaRepository:

    @classmethod

    def insert_alternative(self, new_alternative:Alternativa)->None:

        try:
             with DBConnectionHandler() as database:
                 
                 database.session.add(new_alternative)
                 database.session.commit()

        except Exception as exception:
            database.session.rollback()
            raise exception