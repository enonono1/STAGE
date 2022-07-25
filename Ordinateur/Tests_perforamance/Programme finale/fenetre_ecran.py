
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:14:44 2022

@author: enora
"""
import tkinter as tk
from screeninfo import get_monitors


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
        
    def get_monitor_from_coord(self,x, y):
        monitors = get_monitors()

        for m in reversed(monitors):
            if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
                return m
        return monitors[0] 
    
    def create_animation_window(self):
        """
        créer une fenêtre animé
        Arguments :
        None
        Returns :
        la fenêtre créée
        """
        Window = tk.Tk()
        x = Window.winfo_x()
        y = Window.winfo_y()
        
        # Get the screen which contains top
        current_screen = self.get_monitor_from_coord(x, y)

        # Get the monitor's size
        w = current_screen.width
        h = current_screen.height
        
        self.width = w
        self.height = h
        
        Window.title("Eye tracking")
        Window.geometry(f'{w}x{h}')
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