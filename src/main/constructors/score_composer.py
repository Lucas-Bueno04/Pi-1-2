from src.controller.ScoreController import ScoreController
from src.view.app_views.ScoreFrame import ScoreFrame
from typing import Callable

def score_composer(master,return_command):

    controller = ScoreController(view=ScoreFrame(master=master), return_command=return_command)

    return controller