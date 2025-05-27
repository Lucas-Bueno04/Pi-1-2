from src.view.app_views.HomeFrame import HomeFrame
from src.view.app_views.Windown import Windown
from src.view.app_views.QuestionFrame import QuestionFrame
from src.controller.RodadaController import RodadaController
from src.model.repositories.questao_repo import QuestaoRepository


def round_composer(master:Windown, end_function):

    question_repository = QuestaoRepository()
    controller = RodadaController(master=master, model=question_repository,end_function=end_function)

    return controller