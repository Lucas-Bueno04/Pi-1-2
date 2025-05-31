import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image


class Telalogin(ctk.CTkFrame):

    def __init__(self, master, width = settings['MainWidth'], height = settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        
        self.bg_img = ctk.CTkImage(dark_image=Image.open("src/assets/login_frame.png"), light_image=Image.open("src/assets/login_frame.png"), size=(settings['MainWidth'],settings['MainHeight']))

        self.login_label = ctk.CTkLabel(
            master=self, 
            text="", 
            image=self.bg_img,
            width=settings['MainWidth'],
            height=settings['MainHeight']
        )

        self.login_label.place(x = 0,y = 0)

        self.login_label_text = ctk.CTkLabel(
            master=self.login_label,
            width=300, 
            height=50, 
            text='LOGIN',
            font=('Roboto', 52, 'bold'), 
            text_color="#FFFFFF", 
            bg_color="#003e6a", 
            fg_color="#003e6a"
        )
        self.login_label_text.place( x = 600, y = 100)

        self.login_entry = ctk.CTkEntry(
            master = self.login_label, 
            placeholder_text="Email", 
            text_color="#FFFFFF",
            font=settings['ParagraphFont'],
            width=300,
            height=50,
            bg_color="#003e6a",
            fg_color="#003e6a"
        )
        self.login_entry.place(x = 600, y = 200)

        self.password_entry = ctk.CTkEntry(
            master = self.login_label, 
            placeholder_text="Senha", 
            text_color="#FFFFFF",
            font=settings['ParagraphFont'],
            width=300,
            height=50,
            bg_color="#003e6a",
            fg_color="#003e6a"

        )

        self.password_entry.place(x = 600, y = 300)
