from src.view.app_views.ScoreFrame import ScoreFrame
from typing import Callable
from datetime import date, datetime
import json
from src.model.repositories.rodada_repo import RodadaRepository
from src.model.entities.rodada import Rodada

class ScoreController:


    def __init__(self, view:ScoreFrame, return_command:Callable):
        
        self.view = view
        self.return_command = return_command
        self.__rodada_repo = RodadaRepository()
        self.score = None
    
    def show_view(self, score):
        self.score = int(score)
        self.view.update_score(score)
        self.view.update_return_funcion(self.play_again)
        self.view.place(x = 0, y = 0)

    def play_again(self):
        
        self.save_score_history(self.score)
        self.view.destroy()
        self.return_command()

            
    def save_score_history(self, score):

        current_user_id = self.get_current_user_id()

        data = datetime.today().date()

        new_rodada = Rodada(pontuacao = score, data = data, id_usuario=current_user_id)
        try:
            self.__rodada_repo.insert_round(new_rodada)
        except Exception as e:
            raise e

    
        
    
    def get_current_user_id(self):

        with open("cache.json", "r", encoding="utf-8") as cache:

            dados = json.load(cache)

        current_user_id = dados['USER_ID']

        return current_user_id