
from src.view.app_views.RankingFrame import RankingFrame
from src.model.repositories.rodada_repo import RodadaRepository


def ranking_composer(master, back_command=None, get_registries_command =None):


    frame = RankingFrame(master=master, back_command=back_command, get_registries_command=get_registries_command )
    return frame