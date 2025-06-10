
from src.model.repositories.rodada_repo import RodadaRepository
from src.controller.GetHistoryController import GetHistoryController

def get_history_composer():

    repo = RodadaRepository()
    controller = GetHistoryController(repo)

    return controller