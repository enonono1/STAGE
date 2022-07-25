# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:30:28 2022

@author: enora
"""

import time

class suivi_ecran(object):
    
    def __init__(self,Animation_dessin,Animation_Window):
        self.Animation_Window_ = Animation_Window
        self.Animation_dessin_ = Animation_dessin
        self.x_prec = 0
        self.y_prec = 0
        self.diam = 20
        self.P = None
        self.p= None
        
    def start(self,x,y,rapport_x,rapport_y):
        Deplacement_x = int(x-self.x_prec)
        Deplacement_y = int(y-self.y_prec)
        
        if self.p == 0 :
            self.P = self.creation_points()
            self.p = 1
        
        mov_x,mov_y = self.mouvement(Deplacement_x,Deplacement_y)
        self.move(Deplacement_x,Deplacement_y,mov_x,mov_y,rapport_x,rapport_y)
        
    def mouvement(self,ecart_x,ecart_y):
        if ecart_x > 0:
            Deplacment_x = -1 #déplacement negatif

        elif ecart_x == 0:
            Deplacment_x = 0 #déplacement negatif

        else:
            Deplacment_x = 1 #déplacement positif

        
        if ecart_y > 0:
            Deplacment_y = -1 #déplacement negatif

        elif ecart_y == 0:
            Deplacment_y = 0 #déplacement negatif
        
        else:
            Deplacment_y= 1 #déplacement positif
            
        return Deplacment_x,Deplacment_y

    def move(self,x,y,mov_x,mov_y,rapport_x,rapport_y):
            position_x = self.round_to_decimal(x)
            position_y = self.round_to_decimal(y)

            Axinc =(position_x*mov_x*rapport_x)-self.diam/2
            Ayinc =(position_y*mov_y*rapport_y)-self.diam/2
            
            des =  self.Animation_dessin_ 
            
           #des.move(self.P,Axinc,Ayinc)

            self.Animation_Window_.update()
            
            time.sleep(1)

    def round_to_decimal(self,n):  
        return (int(n/10))*10
