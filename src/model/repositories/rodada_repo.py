from src.model.entities.rodada import Rodada
from src.model.settings.connection import DBConnectionHandler
from typing import List



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
        

    @classmethod

    def show_all(self)->List[Rodada]:

        try:

            with DBConnectionHandler() as database:

                registries = database.session.query(Rodada).all()

                return registries
            
        except Exception as exception:

            database.session.rollback()
            raise exception

