import customtkinter as ctk
import tkinter as tk
from src.view.app_views.app_view_settings import settings


class Windown(ctk.CTk):

    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry(f'{settings['MainWidth']}x{settings["MainHeight"]}')

        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_appearance_mode("dark")

        self.title("Jogo Do Milhão")

        self.resizable(False, False)