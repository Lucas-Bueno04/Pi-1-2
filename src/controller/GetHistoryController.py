
from src.model.repositories.rodada_repo import RodadaRepository
from src.model.repositories.usuario_repo import UserRepository

class GetHistoryController:

    def __init__(self, rodada_repo :RodadaRepository ):
        self.__rodada_repo = rodada_repo
        self.__user_repo = UserRepository()
    
    def handle(self ):


        registries = self.__rodada_repo.show_all()

        lista_strings = []
        for rodada in registries:
            nome_usuario = self.__user_repo.get_user_by_id(rodada.id_usuario).nome  # Supondo que tenha relationship configurada
            pontuacao = rodada.pontuacao
            data = rodada.data.strftime("%Y-%m-%d")  # formatar data como string

            registry = (pontuacao,nome_usuario, data)

            lista_strings.append(registry)
        
        return lista_strings