from src.view.app_views.AddQuestFrame import AddQuestFrame



def add_question_composer(master, back_command=None, insert_command=None):

    frame = AddQuestFrame(master=master, back_command=back_command, insert_command=insert_command)
    return frame