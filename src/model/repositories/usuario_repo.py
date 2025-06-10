from src.model.entities.usuario import Usuario
from src.model.settings.connection import DBConnectionHandler



class UserRepository:

    @classmethod

    def insert_user(self, new_user_registry:Usuario)->None:

        with DBConnectionHandler() as database:
            try:
                database.session.add(new_user_registry)
                database.session.commit()

            
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    
    @classmethod

    def get_user_by_email(self, email):

        with DBConnectionHandler() as database:

            try:

                usuario = database.session.query(Usuario).filter(Usuario.email == email).one()

                return usuario

            except Exception as exception:

                database.session.rollback()
                raise exception
    

    @classmethod

    def get_user_by_id(self, id_user):

        with DBConnectionHandler() as database:

            try:

                usuario = database.session.query(Usuario).filter(Usuario.id == id_user).one()

                return usuario

            except Exception as exception:

                database.session.rollback()
                raise exception
    