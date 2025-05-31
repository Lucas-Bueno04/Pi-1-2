import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable

class ScoreFrame(ctk.CTkFrame):

    def __init__(self, master,
                 score=None, 
                 play_again_command=None,
                 width = settings["MainWidth"], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "transparent" , fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.score = score
        
        self.play_again_command = play_again_command

        self.background_image = ctk.CTkImage(
            light_image=Image.open("src/assets/score_frame.png"),
            dark_image=Image.open("src/assets/score_frame.png"),
            size=(width, height)
        )

        self.background_label = ctk.CTkLabel(
            master=self,
            text=None,
            image=self.background_image,
            width=width,
            height=height
        )
        self.background_label.place(x=0, y=0)

        self.score_label = ctk.CTkLabel(
            master = self,
            width=400, 
            height=50, 
            text=f"Score: {self.score}",
            text_color="#FFFFFF",
            font=('Roboto', 28, 'bold'),
            bg_color="#003e6a",
            fg_color="#003e6a",
        )

        self.score_label.place(x = 312, y = 300)


        
        self.play_again_btn = ctk.CTkButton(
            master = self, 
            width=400, 
            height=100,
            text="JOGAR NOVAMENTE",
            text_color="#FFFFFF",
            bg_color="#003e6a",
            fg_color="#DF650E",
            corner_radius=20,
            font=('Roboto', 28, 'bold'),
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