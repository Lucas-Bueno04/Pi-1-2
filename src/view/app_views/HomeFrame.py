import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable

class HomeFrame(ctk.CTkFrame):

    def __init__(self, master, 
                 start_command:Callable=None,
                 width =settings['MainWidth'] , height = settings["MainHeight"], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.start_command = start_command

        self.main_label_img = ctk.CTkImage(dark_image=Image.open("src/assets/home_frame6.png"), light_image=Image.open("src/assets/home_frame4.png"), size=(settings['MainWidth'],settings['MainHeight']))


        self.main_label = ctk.CTkLabel(
            master = self, 
            text=None, 
            width=settings["MainWidth"],
            height=settings["MainHeight"],
            image=self.main_label_img
        )

        self.main_label.place(x = 0, y = 0)

        self.title_home_label = ctk.CTkLabel(
            master=self, 
            text='POLIEDRO',
            width=300, 
            height=100,
            font=("Arial", 52),
            text_color="#000000",
            bg_color="#EEECFA",
            fg_color="#EEECFA",
            corner_radius=20
        )

        self.title_home_label.place(x=362, y = 200)
        
        self.play_btn = ctk.CTkButton(
            master = self, 
            width=300, 
            height=100,
            text="JOGAR",
            text_color="#000000",
            bg_color="#EEECFA",
            fg_color="#FFCB7C",
            corner_radius=20,
            font=settings['HeaderFont'],
            hover_color="#F12754",
            command=self.start_command
        )

        self.play_btn.place(x=362, y = 400 )