# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:20:34 2022

@author: enora
"""


class Point(object):
    def __init__(self, abs1, ord1,abs2, ord2,diam,canvas,cote):
        self.A = (abs1,ord1)
        self.B = (abs2,ord2)
        self.Canvas = canvas
        self.P = self.Canvas.create_oval(self.A,self.B, fill='red', outline='red', width=2)
        self.c = cote  # 1 = Gauche , 0 = Droite
        self.x = abs1 + (diam/2) #coordonnées du milieu du point
        self.y = ord1 + (diam/2) #coordonnées du milieu du point
    def pos_point(self):
        A,B,C,D = self.Canvas.coords(self.P)
        return A,B,C,D