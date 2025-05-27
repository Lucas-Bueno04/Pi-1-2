from src.main.constructors.round_controler_composer import round_composer
from src.main.constructors.windown_composer import windown_composer
from src.main.constructors.home_composer import home_composer
from src.main.constructors.score_composer import score_composer


class ProcessHandler:

    def __init__(self):
        
        self.windown = windown_composer()
        self.home = None
        self.score = None
    
    def clear(self, ):

        if self.home and self.home.winfo_exists():
            self.home.destroy()

    
    def show_home(self):
        
        self.home = home_composer(master=self.windown, start_command=self.sample_questions)
        self.home.place(x = 0, y = 0)

    def show_score(self, pontuation):
        self.score = score_composer(master=self.windown,return_command=self.show_home)
        self.score.show_view(score = pontuation)
        


    def sample_questions(self, ):

        self.clear()

        self.round_controller = round_composer(master=self.windown,end_function=self.show_score)
    
    def start(self):
        
        self.show_home()

        self.windown.mainloop()