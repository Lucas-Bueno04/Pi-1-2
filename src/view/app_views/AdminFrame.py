import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable


class AdminFrame(ctk.CTkFrame):

    def __init__(self, master, width = settings['MainWidth'], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)


        self.bg_img = ctk.CTkImage(dark_image=Image.open("src/assets/bgimage.jpeg"), light_image=Image.open("src/assets/bgimage.jpeg"), size=(settings['MainWidth'],settings['MainHeight']))

        self.background_label = ctk.CTkLabel(
            master=self, 
            width=settings['MainWidth'],
            height=settings['MainHeight'],
            text=None,
            image=self.bg_img
        )
        self.background_label.place(x = 0, y = 0)

        self.logo_poliedro = ctk.CTkImage(dark_image=Image.open("src/assets/logo_poliedro.png"), light_image=Image.open("src/assets/logo_poliedro.png"), size=(200,200))

        self.logo_poliedro_label = ctk.CTkLabel(
            master = self.background_label,
            width=200,
            height=200, 
            text=None,
            fg_color="#003E69",
            bg_color="#003E69",
            image=self.logo_poliedro,
        )
        self.logo_poliedro_label.place(x = 412, y = 50)

        self.editar_questão_button = ctk.CTkButton(master=self, 
                                                   width=300, 
                                                   height=50, 
                                                   text='Editar Questão', 
                                                   font=settings['HeaderFont'],
                                                   bg_color="#003E69", 
                                                   fg_color="#FF6F00", 
                                                   corner_radius=10, hover_color='#F12754')
        
        self.editar_questão_button.place(x = 362, y = 250)

        self.cadastrar_alunos_button = ctk.CTkButton(master=self,
                                                     width=300, 
                                                   height=50, 
                                                   text='Cadastrar Aluno', 
                                                   font=settings['HeaderFont'],
                                                   bg_color="#003E69", 
                                                   fg_color="#FF6F00", 
                                                   corner_radius=10, hover_color='#F12754'
                                                     )
        
        self.cadastrar_alunos_button.place( x = 362, y =350 )

        self.exibir_ranking_button = ctk.CTkButton(
            master = self, 
            width=300, 
            height=50, 
            text='Mostrar Ranking', 
            font=settings['HeaderFont'],
            bg_color="#003E69", 
            fg_color="#FF6F00", 
            corner_radius=10, hover_color="#F12754"
        )
        self.exibir_ranking_button.place(x = 362, y = 450 )