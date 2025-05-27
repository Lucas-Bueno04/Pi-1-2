from src.view.app_views.QuestionFrame import QuestionFrame
from src.model.repositories.questao_repo import QuestaoRepository
from src.model.entities.questao import Questao
from src.model.entities.alternativa import Alternativa  
import customtkinter as ctk
import tkinter as tk
from src.model.usecases.Randomize import Randomize
from typing import Callable


class RodadaController:
    
    def __init__(self, master:ctk.CTk, model:QuestaoRepository, end_function:Callable=None):  
        self.end_function = end_function

        self.master = master

        self.pontuation = 0

        self.current_index = 0
        self.current_frame = None

        self.questions = []

        self.sample_questions()
        self.show_next_question()

    
    def sample_questions(self):

        questions = QuestaoRepository.get_all()
        
        for question in questions:
            question_dict = {
                "QuestionTitle":question.enunciado,
                "Answers":[]
            }

            for alternativa in question.alternativas:
                answer_dict = {
                    "Id":alternativa.id,
                    "Title":alternativa.enunciado,
                    "Type":alternativa.verify,
                    "Status":"visible"
                }
                question_dict["Answers"].append(answer_dict)

            self.questions.append(question_dict)

    def show_next_question(self, ):

        self.questions = Randomize.draw(list=self.questions)

        if self.current_frame:
            self.current_frame.destroy()  

        if self.current_index < len(self.questions):
            question_data = self.questions[self.current_index]

            self.current_frame = QuestionFrame(
                master=self.master,
                question_params=question_data,
                on_answer=self.handle_answer
            )

            self.current_frame.pack(fill="both", expand=True)
            self.override_button_behavior(self.current_frame)

            self.current_index += 1
        else:
            # Fim das perguntas
            self.show_end_screen()

    def override_button_behavior(self, frame):
         for child in frame.winfo_children():
            if isinstance(child, ctk.CTkButton):
                original_command = child.cget("command")
                def new_command(original_cmd=original_command, btn=child):
                    btn.after(800, self.show_next_question)  
                    original_cmd()
                child.configure(command=new_command)

    def handle_answer(self, is_correct):
        if is_correct:
            self.pontuation += 5
            print(f"Resposta correta! Pontuação atual: {self.pontuation}")
        else:
            print(f"Resposta errada. Pontuação atual: {self.pontuation}")

        self.master.after(800, self.show_next_question)

    def show_end_screen(self):
        
        self.end_function(self.pontuation)

    

        

        

            
