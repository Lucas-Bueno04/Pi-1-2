from src.model.repositories.usuario_repo import UserRepository
from src.model.entities.usuario import Usuario
import bcrypt

def insert():

    email = "admin@admin"
    nome = "Admin"
    password = "adminpoliedro".encode()
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    type = 1
    
    new_user = Usuario(
        email = email, 
        nome = nome,
        senha = password,
        type = type
    )
    UserRepository.insert_user(new_user_registry=new_user)
    print("USUARIO ADMIN CADASTRADO COM SUCESSO")