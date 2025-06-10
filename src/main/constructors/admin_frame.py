from src.view.app_views.AdminFrame import AdminFrame



def admin_composer(master, show_add_question = None, show_cad_aluno =None, show_ranking = None):

    a = AdminFrame(master=master, show_cad_aluno=show_cad_aluno, show_add_question=show_add_question, show_ranking=show_ranking)
    return a