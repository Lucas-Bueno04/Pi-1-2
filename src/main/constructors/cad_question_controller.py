from src.model.repositories.questao_repo import QuestaoRepository
from src.model.repositories.alternativa_repo import AlternativaRepository
from src.controller.CadQuestionController import CadQustionController


def cad_question_controller_composer():

    question_repo = QuestaoRepository()
    alternative_repo = AlternativaRepository()

    controller = CadQustionController(question_repo=question_repo, alternativa_repo=alternative_repo)

    return controller