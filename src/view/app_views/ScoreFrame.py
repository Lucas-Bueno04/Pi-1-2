import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from typing import Callable
from PIL import Image

class ScoreFrame(ctk.CTkFrame):

    def __init__(self, master,
                 score=None, 
                 play_again_command=None,
                 width = settings["MainWidth"], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color ="#052159" , fg_color = "#052159", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.score = score
        
        self.play_again_command = play_again_command

        self.endgame_img = ctk.CTkImage(dark_image=Image.open("src/assets/Frame 21.png"), light_image=Image.open("src/assets/Frame 21.png"), size=(settings['MainWidth'],settings['MainHeight']))
        
        self.background_label = ctk.CTkLabel(
            master=self, 
            width=settings['MainWidth'],
            height=settings['MainHeight'],
            text=None,
            image=self.endgame_img
        )
        self.background_label.place(x = 0, y = 0)

        self.end_game_title = ctk.CTkLabel(
            master=self.background_label, 
            width=400,
            height=50,
            text="Fim de Jogo!",
            text_color="#000000",
            font=settings["HeaderFont"],
            bg_color="#EEECFA",
            fg_color="#EEECFA",
        )

        self.end_game_title.place(x =312, y = 200 )

        self.score_label = ctk.CTkLabel(
            master = self.background_label,
            width=400, 
            height=50, 
            text=f"Score: {self.score}",
            text_color="#000000",
            font=settings["HeaderFont"],
            bg_color="#EEECFA",
            fg_color="#EEECFA",
        )

        self.score_label.place(x = 312, y = 300)


        
        self.play_again_btn = ctk.CTkButton(
            master = self.background_label, 
            width=400, 
            height=100,
            text="JOGAR NOVAMENTE",
            text_color="#FFFFFF",
            bg_color="#EEECFA",
            fg_color="#FFCB7C",
            corner_radius=20,
            font=settings['HeaderFont'],
            hover_color="#F12754",
            command=self.play_again_command

        )

        self.play_again_btn.place(x = 312, y = 400)

    def update_score(self, score):
        self.score = score
        self.score_label.configure(text=f"Score: {self.score}")

    def update_return_funcion(self, return_funcion):
        self.play_again_command = return_funcion
        self.play_again_btn.configure(command = self.play_again_command)