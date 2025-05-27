from src.model.repositories.alternativa_repo import AlternativaRepository
from src.model.repositories.questao_repo import QuestaoRepository
from src.model.entities.alternativa import Alternativa
from src.model.entities.questao import Questao


class QuestionSampler:

    def __init__(self):
        self.question_database = []

    
    def get_question(self):

        questions = Questao()