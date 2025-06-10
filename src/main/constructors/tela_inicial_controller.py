from src.controller.TypeUserTelaController import TypeUserTelaController

def tela_inicial_composer(admin_frame_command, default_frame_command):

    t = TypeUserTelaController(admin_frame=admin_frame_command, default_frame=default_frame_command)
    return t
