from src.view.app_views.CadAlunoFrame import CadAlunoFrame



def cad_aluno_composer(master, back_command = None, insert_command=None ):

    frame = CadAlunoFrame(master=master, back_command=back_command, insert_command=insert_command)
    return frame