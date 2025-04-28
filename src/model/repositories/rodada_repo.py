from src.model.entities.rodada import Rodada
from src.model.settings.connection import DBConnectionHandler




class RodadaRepository:

    @classmethod

    def insert_round(self, new_round:Rodada)->None:

        try:

            with DBConnectionHandler() as database:

                database.session.add(new_round)
                database.session.commit()

    
        except Exception as exception:

            database.session.rollback()
            raise exception
        
