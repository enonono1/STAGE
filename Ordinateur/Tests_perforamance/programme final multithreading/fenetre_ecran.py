
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:14:44 2022

@author: enora
"""
import tkinter as tk
from win32api import GetSystemMetrics 


class Fenetre_ecran(object):
    def __init__(self):
        self.width = None
        self.height = None
        self.Animation_canvas = None
        self.Animation_Window = None
        
        self.initialisation()

    def initialisation(self):
        """
        récupère les dimensions de l'écran de l'utilisateur puis vient créer une fenêtre animé et un dessin dedans
        Arguments :
        None
        Returns :
        None
        """
        self.Animation_Window= self.create_animation_window()
        self.Animation_canvas = self.create_animation_canvas(self.Animation_Window)
        
    def create_animation_window(self):
        """
        créer une fenêtre animé
        Arguments :
        None
        Returns :
        la fenêtre créée
        """
        Window = tk.Tk()
        
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        
        Window.title("Eye tracking")
        Window.geometry(f'{self.width}x{self.height}')
        return Window
 

    def create_animation_canvas(self,Window):
        """
        créer une fenêtre animé
        Arguments :
        Window
        Returns :
        le canvas crée
        """
        canvas = tk.Canvas(Window)
        canvas.configure(bg="black")
        canvas.pack(fill="both", expand=True)
        return canvas