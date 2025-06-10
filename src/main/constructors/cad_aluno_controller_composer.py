from src.model.repositories.usuario_repo import UserRepository
from src.controller.CadAlunoController import CadAlunoController
def cad_aluno_controller_composer():

    controller = CadAlunoController(user_repo=UserRepository())
    return controller