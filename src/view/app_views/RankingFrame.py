import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable

class RankingFrame(ctk.CTkFrame):

    def __init__(self, master, width = settings["MainWidth"], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
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

                # Estilo do Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Cabeçalho
        self.style.configure("Treeview.Heading", 
            background="#FF6F00", 
            foreground="white", 
            font=('Arial', 12, 'bold')
        )

        # Células
        self.style.configure("Treeview", 
            background="#2B2B2B", 
            foreground="white", 
            rowheight=30, 
            fieldbackground="#2B2B2B", 
            font=('Arial', 11)
        )

        self.ranking_table = ttk.Treeview(self.background_label, columns=("Pontuação", "Nome", "Data"), show="headings")

        self.ranking_table.heading("Pontuação", text="Pontuação")
        self.ranking_table.heading("Nome", text="Nome")
        self.ranking_table.heading("Data", text="Data")

        self.ranking_table.column("Pontuação", width=300)
        self.ranking_table.column("Nome", width=300)
        self.ranking_table.column("Data", width=300)


        self.ranking_table.place(x = 62, y =50 )

        self.back_img = ctk.CTkImage(dark_image=Image.open("src/assets/picon_back.png"), light_image=Image.open("src/assets/picon_back.png"), size=(50,50))
        self.back_buttom = ctk.CTkButton(
            master = self.background_label, 
            text=None, 
            bg_color="#003E69",
            fg_color="#003E69",
            width=50, 
            height=50,
            image=self.back_img
        )

        self.back_buttom.place(x =462, y = 500 )
