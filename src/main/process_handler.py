from src.main.constructors.round_controler_composer import round_composer
from src.main.constructors.windown_composer import windown_composer
from src.main.constructors.home_composer import home_composer
from src.main.constructors.score_composer import score_composer
from src.main.constructors.login_controller import login_composer
from src.main.constructors.tela_login_composer import tela_login_composer
from src.main.constructors.tela_inicial_controller import tela_inicial_composer
from src.main.constructors.admin_frame import admin_composer
from src.main.constructors.edit_question_composer import add_question_composer
from src.main.constructors.cad_aluno_composer import cad_aluno_composer
from src.main.constructors.ranking_composer import ranking_composer
from src.main.constructors.cad_aluno_controller_composer import cad_aluno_controller_composer
from src.main.constructors.cad_question_controller import cad_question_controller_composer
from src.main.constructors.get_history_composer import get_history_composer

class ProcessHandler:

    def __init__(self):
        
        self.windown = windown_composer()
        self.home = None
        self.score = None
        self.admin = None
        self.add_question_frame = None
        self.ranking_frame = None
        self.login = None
        self.cad_aluno_frame = None
    
    def clear(self, ):

        if self.home and self.home.winfo_exists():
            self.home.destroy()
        
        if self.admin and self.admin.winfo_exists():
            self.admin.destroy()

        if self.add_question_frame and self.add_question_frame.winfo_exists():
            self.add_question_frame.destroy()

        if self.ranking_frame and self.ranking_frame.winfo_exists():
            self.ranking_frame.destroy()
        
        if self.login and self.login.winfo_exists():
            self.login.destroy()
        
        if self.cad_aluno_frame and self.cad_aluno_frame.winfo_exists():
            self.cad_aluno_frame.destroy()
        


    
    def show_home(self):

        self.clear()
        
        self.home = home_composer(master=self.windown, start_command=self.sample_questions)
        self.home.place(x = 0, y = 0)

    def show_admin(self):
        self.clear()
        
        self.admin = admin_composer(master=self.windown, show_add_question=self.show_edit_question_frame, show_cad_aluno=self.show_cad_aluno, show_ranking=self.show_ranking_frame)
        self.admin.place(x = 0, y = 0)

    def show_score(self, pontuation):
        self.clear()
        
        self.score = score_composer(master=self.windown,return_command=self.show_home)
        self.score.show_view(score = pontuation)
        

    def show_tela_inicial(self, ):
        self.clear()
        
        t = tela_inicial_composer(admin_frame_command=self.show_admin, default_frame_command=self.show_home)
        t.handle()

    def show_edit_question_frame(self, ):
        self.clear()
        
        self.add_question_frame = add_question_composer(master=self.windown, back_command=self.show_tela_inicial, insert_command=cad_question_controller_composer().handle)
        self.add_question_frame.place(x = 0, y = 0)

    def show_cad_aluno(self, ):
        self.clear()
        
        self.cad_aluno_frame = cad_aluno_composer(master=self.windown, back_command=self.show_tela_inicial, insert_command=cad_aluno_controller_composer().handle)
        self.cad_aluno_frame.place(x = 0, y = 0)

    def show_ranking_frame(self):
        self.clear()
        

        self.ranking_frame = ranking_composer(master=self.windown, back_command=self.show_tela_inicial, get_registries_command=get_history_composer().handle)
        self.ranking_frame.place(x = 0, y = 0)

    def sample_questions(self, ):

        self.clear()

        self.round_controller = round_composer(master=self.windown,end_function=self.show_score)

    def show_login(self, ):
        self.clear()
        

        login = login_composer()
        self.login = tela_login_composer(master=self.windown, login__command=login.handler, next_frame_command = self.show_tela_inicial)
        self.login.place(x = 0, y = 0)
    

    
    def start(self):
        
        self.show_login()

        self.windown.mainloop()