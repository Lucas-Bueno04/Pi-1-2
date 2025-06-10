from src.model.repositories.questao_repo import QuestaoRepository
from src.model.repositories.alternativa_repo import AlternativaRepository
from src.model.entities.questao import Questao
from src.model.entities.alternativa import Alternativa
from tkinter import messagebox

class CadQustionController:

    def __init__(self , question_repo:QuestaoRepository, alternativa_repo = AlternativaRepository):
        
        self.__question_repo = question_repo
        self.__alternativa_repo = alternativa_repo

    
    def handle(self, enunciado, dica, materia, list_alternatives):
        
        try:
            question = Questao(enunciado=enunciado, dica = dica,  materia=materia)

            self.__question_repo.insert_question(new_question=question)

            id_question = self.__question_repo.get_question_id_by_enunciado(enunciado=enunciado)

            for alternativa in list_alternatives:

                new_alternativa = Alternativa(q_id = id_question, enunciado = alternativa[0], verify = alternativa[1])

                self.__alternativa_repo.insert_alternative(new_alternative=new_alternativa)
            
            messagebox.showinfo(title="Cadastro Questão", message="Questão Cadastrada com Sucesso!")

        except Exception as e:

            messagebox.showerror("Cadastro pergunta", message="Não foi possivel concluir o cadastro de perguntas, verifique as entradas de valores")

            raise e
            
