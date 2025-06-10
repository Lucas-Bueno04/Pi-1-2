from src.model.repositories.usuario_repo import UserRepository
from src.model.entities.usuario import Usuario
import bcrypt
from tkinter import messagebox



class CadAlunoController:

    def __init__(self, user_repo:UserRepository):
        self.__user_repo = user_repo

    
    def handle(self, email,name,  password, confirm_password):
        
        if self.__check_confirm_password(password, confirm_password):
            
            new_user = self.__construct_user(email = email, name=name, password=password, type=False)

            try:
                self.__insert_repo(new_user=new_user)
                
            except Exception as e:
                messagebox.showerror("Cadastro Aluno", message="Não foi possivel completar o cadastro do aluno")
                raise e
        else:
            messagebox.showerror(title="Cadastro Aluno", message="Senhas Divergentes")
    
    def __check_confirm_password(self, password, confirm_password):

        return password == confirm_password
    
    def __construct_user(self, email,name, password, type):

        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        new_user = Usuario(
            email = email, 
            nome = name, 
            senha = password, 
            type = type
        )
        
        return new_user
    

    def __insert_repo(self, new_user):

        self.__user_repo.insert_user(new_user)
        messagebox.showinfo(title="Cadastro Aluno", message="Usuario Cadastrado com Sucesso!")
