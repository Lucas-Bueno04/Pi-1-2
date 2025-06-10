from src.view.app_views.TelaLogin import Telalogin


def tela_login_composer(master, login__command, next_frame_command):

    return Telalogin(master=master, login_command=login__command, next_frame_command=next_frame_command)