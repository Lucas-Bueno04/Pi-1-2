import bcrypt
from src.view.app_views.TelaLogin import Telalogin
from src.model.repositories.usuario_repo import UserRepository
import json
from tkinter import messagebox
from typing import Callable
class LoginController:

    def __init__(self, user_repo:UserRepository):
        
        self.__user_repo = user_repo
    
    def handler(self, user_email, user_password, next_tela_command):

        try: 
            usuario = self.__user_repo.get_user_by_email(email=user_email)
            compare = self.__compare(user_password, usuario.senha)

            if compare == 1:
                self.__insert_log(user_id=usuario.id, user_type=usuario.type)
                next_tela_command()

            else:
                messagebox.showerror(title="Login", message="Email ou Senha incorretos!")
                

        
        except Exception as e:

            raise e


    
    def __compare(self, password, hashed_password):
    
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            return 1
        
        else:
            return 0
        
    def __insert_log(self, user_id, user_type):

        with open("cache.json", "r", encoding="utf-8") as cache:
            dados = json.load(cache)
        
        dados['USER_ID'] = user_id
        dados['TYPE_USER'] = user_type
    
        with open('cache.json', "w", encoding='utf-8') as cache:
            json.dump(dados, cache, ensure_ascii=False, indent=4)