import tkinter as tk
import customtkinter as ctk
from src.view.app_views.app_view_settings import settings


class QuestionFrame(ctk.CTkFrame):

    def __init__(self, master,
                 question_params,
                 on_answer, 
                 width = settings['MainWidth'], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "#052159", fg_color = "#052159", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.on_answer = on_answer
        self.question_params = question_params


        self.question_title = ctk.CTkLabel(
            master = self, 
            width=400,
            height=50,
            text= self.question_params['QuestionTitle'],
            font=settings["HeaderFont"],
            text_color="#FFFFFF",
            bg_color="#052159",
            fg_color="#052159",
            wraplength=400,
        )

        self.question_title.place(x = 312, y = 50)

        init_place_height = 150
    
        for answer in self.question_params['Answers']:
            
            if answer['Status'] == "visible":
                option_button = ctk.CTkButton(
                    master=self, 
                    width=400,
                    height=50, 
                    text=f"{answer['Id']}.{answer['Title']}",
                    font=settings['ParagraphFont'],
                    text_color="#FFFFFF",
                    fg_color="#FF6F00",
                    hover_color="#F12754",
                )
                option_button.configure( command=lambda is_correct=answer["Type"], b=option_button: self.on_answer_click(is_correct, b))
                option_button.place(x=312, y=init_place_height)

                # Atualiza a altura para o próximo botão
                init_place_height += 60  # 50 da altura + 10 de espaçamento
                
            
                
    def on_answer_click(self, is_correct, button):

        if is_correct:
            button.configure(fg_color="green", text="✅ Correto!")
        else:
            button.configure(fg_color="red", text="❌ Errado!")

        if self.on_answer:
            self.on_answer(is_correct)