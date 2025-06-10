import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable

class CadAlunoFrame(ctk.CTkFrame):

    def __init__(self, master, insert_command=None, back_command=None, width = settings['MainWidth'], height =settings['MainHeight'], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.back_command = back_command
        self.insert_command = insert_command

        self.bg_img = ctk.CTkImage(dark_image=Image.open("src/assets/bgimage.jpeg"), light_image=Image.open("src/assets/bgimage.jpeg"), size=(settings['MainWidth'],settings['MainHeight']))

        self.background_label = ctk.CTkLabel(
            master=self, 
            width=settings['MainWidth'],
            height=settings['MainHeight'],
            text=None,
            image=self.bg_img
        )
        self.background_label.place(x = 0, y = 0)


        self.novo_aluno_label = ctk.CTkLabel(
            master=self.background_label,
            text='Cadastro de Aluno:',
            text_color="#FFFFFF",
            font=settings['HeaderFont'],
            width=300, 
            height=50, 
            bg_color='#003E69',
            fg_color="#003E69"
        )

        self.novo_aluno_label.place(x = 362, y = 50)

        self.email_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300, 
            height=50, 
            placeholder_text="Email",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )
        self.email_entry.place(x = 362, y = 170)
        
        self.nome_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300, 
            height=50, 
            placeholder_text="Nome",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )
        self.nome_entry.place(x = 362, y = 230)
        

        self.password_entry = ctk.CTkEntry(
            master=self.background_label,
            width=300, 
            height=50, 
            placeholder_text="Senha",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.password_entry.place( x = 362, y = 290)

        self.password_confirm_entry = ctk.CTkEntry(
            master = self.background_label,
            width=300,
            height=50, 
            placeholder_text="Confirmar Senha",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.password_confirm_entry.place(x = 362, y = 350)

        self.send_button = ctk.CTkButton(master=self.background_label,
                                         width=300, 
                                         height=50, 
                                         text="Salvar", 
                                         font=settings['ParagraphFont'], bg_color="#003E69", fg_color= "#FF6F00", hover_color="#F12754",
                                         corner_radius=10,
                                         command=self.__cadastrar,
                                         )
        
        self.send_button.place(x =362, y = 420 )

        self.back_img = ctk.CTkImage(dark_image=Image.open("src/assets/picon_back.png"), light_image=Image.open("src/assets/picon_back.png"), size=(50,50))
        self.back_buttom = ctk.CTkButton(
            master = self.background_label, 
            text=None, 
            bg_color="#003E69",
            fg_color="#003E69",
            width=50, 
            height=50,
            image=self.back_img,
            command=self.back_command
        )

        self.back_buttom.place(x =462, y = 500 )

    def __cadastrar(self):

        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.password_confirm_entry.get()
        nome = self.nome_entry.get()

        try:
            self.insert_command(email = email, password = password, confirm_password = confirm_password, name = nome)
            self.__clear()
            
        except Exception as e:
            raise e
    def __clear(self, ):

        self.email_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.password_confirm_entry.delete(0, "end")
        self.nome_entry.delete(0, "end")