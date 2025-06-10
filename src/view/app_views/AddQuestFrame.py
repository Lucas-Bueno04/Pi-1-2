import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings
from PIL import Image
from typing import Callable

class AddQuestFrame(ctk.CTkFrame):

    def __init__(self, master, insert_command=None, back_command = None, width = settings['MainWidth'], height = settings["MainHeight"], corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
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

        self.text_label = ctk.CTkLabel(
            master=self.background_label,
            width=300, 
            height=50, 
            font=settings["HeaderFont"],
            text="Adicionar Questão",
            text_color="#FFFFFF",
            bg_color="#003E69",
            fg_color="#003E69"
        )

        self.text_label.place(x = 362, y = 10)

        self.pergunta_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=600,
            height=30,
            placeholder_text="Questão:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.pergunta_entry.place(x = 212, y = 70)

        self.dica_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=600,
            height=30,
            placeholder_text="Dica:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.dica_entry.place(x = 212, y = 120)

        self.opt1_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Opção 1:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.opt1_entry.place(x = 312, y = 170)
        
        
        self.check1 = ctk.CTkOptionMenu(
            master=self.background_label,
            width=50,
            height=30,
            values=['V','F'],
            fg_color="#FF6F00",
            bg_color="#003E69",
            text_color="#ffffff",
            corner_radius=10
        )
        self.check1.place(x = 620, y = 170 )

        self.opt2_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Opção 2:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.opt2_entry.place(x = 312, y = 220)

        self.check2 = ctk.CTkOptionMenu(
            master=self.background_label,
            width=50,
            height=30,
            values=['V','F'],
            fg_color="#FF6F00",
            bg_color="#003E69",
            text_color="#ffffff",
            corner_radius=10
        )
        self.check2.place(x = 620, y = 220 )

        self.opt3_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Opção 3:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.opt3_entry.place(x = 312, y = 270)

        self.check3 = ctk.CTkOptionMenu(
            master=self.background_label,
            width=50,
            height=30,
            values=['V','F'],
            fg_color="#FF6F00",
            bg_color="#003E69",
            text_color="#ffffff",
            corner_radius=10
        )
        self.check3.place(x = 620, y = 270 )

        self.opt4_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Opção 4:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.opt4_entry.place(x = 312, y = 320)

        self.check4 = ctk.CTkOptionMenu(
            master=self.background_label,
            width=50,
            height=30,
            values=['V','F'],
            fg_color="#FF6F00",
            bg_color="#003E69",
            text_color="#ffffff",
            corner_radius=10
        )
        self.check4.place(x = 620, y = 320 )

        self.opt5_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Opção 5:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.opt5_entry.place(x = 312, y = 370)

        self.check5 = ctk.CTkOptionMenu(
            master=self.background_label,
            width=50,
            height=30,
            values=['V','F'],
            fg_color="#FF6F00",
            bg_color="#003E69",
            text_color="#ffffff",
            corner_radius=10
        )
        self.check5.place(x = 620, y = 370 )

        self.materia_entry = ctk.CTkEntry(
            master=self.background_label, 
            width=300,
            height=30,
            placeholder_text="Matéria:",
            corner_radius=10, 
            fg_color="#CFCECD",
            bg_color="#003E69",
            text_color="#000000",
            font=settings['ParagraphFont']
        )

        self.materia_entry.place(x = 362, y = 420)

        self.send_button = ctk.CTkButton(master=self.background_label,
                                         width=300, 
                                         height=50, 
                                         text="Salvar", 
                                         font=settings['ParagraphFont'], bg_color="#003E69", fg_color= "#FF6F00", hover_color="#F12754",
                                         corner_radius=10, 
                                         command=self.__add
                                         )
        
        self.send_button.place(x =362, y = 470 )

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

        self.back_buttom.place(x =462, y = 530 )


    def __add(self, ):

        enunciado = self.pergunta_entry.get()
        dica = self.dica_entry.get()
        materia = self.materia_entry.get()

        lista_option = []

        print(self.check1.get())

        opt1 = (self.opt1_entry.get(), self.___str_para_bool(self.check1.get()))
        lista_option.append(opt1)

        opt2 = (self.opt2_entry.get(), self.___str_para_bool(self.check2.get()))
        lista_option.append(opt2)

        opt3 = (self.opt3_entry.get(), self.___str_para_bool(self.check3.get()))
        lista_option.append(opt3)

        opt4 = (self.opt4_entry.get(), self.___str_para_bool(self.check4.get()))
        lista_option.append(opt4)

        opt5 = (self.opt5_entry.get(), self.___str_para_bool(self.check5.get()))
        lista_option.append(opt5)

        try:
            self.insert_command(enunciado = enunciado, 
                                materia = materia, 
                                dica = dica, 
                                list_alternatives = lista_option
                                )
            
            self.__clear()

        except Exception as e:

            raise e

        

    def __clear(self, ):

        self.pergunta_entry.delete(0, "end")
        self.dica_entry.delete(0, "end")
        self.materia_entry.delete(0, "end")

        self.opt1_entry.delete(0, "end")
        self.opt2_entry.delete(0, "end")
        self.opt3_entry.delete(0, "end")
        self.opt4_entry.delete(0, "end")
        self.opt5_entry.delete(0, "end")


    def ___str_para_bool(self, valor: str) -> bool:
        if valor.strip().upper() == "V":
            return True
        elif valor.strip().upper() == "F":
            return False
        else:
            raise ValueError("Valor inválido: use 'V' para Verdadeiro ou 'F' para Falso.")