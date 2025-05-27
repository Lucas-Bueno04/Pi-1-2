from src.view.app_views.ScoreFrame import ScoreFrame
from typing import Callable



class ScoreController:

    def __init__(self, view:ScoreFrame, return_command:Callable):
        
        self.view = view
        self.return_command = return_command
    
    def show_view(self, score):
        self.view.update_score(score)
        self.view.update_return_funcion(self.play_again)
        self.view.place(x = 0, y = 0)

    def play_again(self):
        
        self.save_score_history()
        self.view.destroy()
        self.return_command()

            
    def save_score_history(self):
        pass