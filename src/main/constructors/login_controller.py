from src.view.app_views.TelaLogin import Telalogin
from src.model.repositories.usuario_repo import UserRepository
from src.controller.LoginController import LoginController


def login_composer():

    repo = UserRepository()

    controller = LoginController(user_repo=repo)

    return controller
