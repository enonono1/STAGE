# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:54:35 2022

@author: enora
"""
import time
from Point import Point

class Calibration_coordonne_vers_ecran(object):
    
    def __init__(self,Animation_canvas_,Animation_Window_,h,w):
        self.width = w
        self.height = h
        self.diam=40
        self.Refresh_Sec = 0.1
        self.xinc = 10
        self.yinc = 10
        self.nb_frames = 30
        self.tab_x= []
        self.tab_y= []
        self.tab_xp_xe = [[120,None],[1800,None],[1800,None],[120,None],[540,None]]
        self.tab_yp_ye = [[120,None],[120,None],[960,None],[960,None],[960,None]]
        self.Animation_canvas = Animation_canvas_
        self.Animation_Window = Animation_Window_
        self.tab_moy_rapport_x = []
        self.tab_moy_rapport_y = []
        self.i = 0
        self.p = 0
        self.P = None
        self.fix = None
 
        
    def calibration_point_termine(self):
        return self.i == 6
        
    def start_calibration(self,x,y):
        moy_rapport_px_x,moy_rapport_px_y = 0,0
        self.tab_x =[]
        self.tab_y =[]
        self.fix = 0
        
        if self.p == 0 :
            self.P = self.creation_points()
            self.p = 1
            
        
        if self.dans_le_cercle(x,y) :
            if not self.fix_point():
                print(self.fix)
                self.recuperation_x_y(x,y)
                self.fix = self.fix + 1
            self.position_x_y_sur_ecran()
            
            rapport_px_x,rapport_px_y = self.calcul_du_rapport()
            moy_rapport_px_x,moy_rapport_px_y = self.calcul_moy_rapport(rapport_px_x,rapport_px_y)
            self.move(self.Animation_Window,self.P,self.Animation_canvas)
            self.retablir_variable()
            
            return moy_rapport_px_x,moy_rapport_px_y

        return moy_rapport_px_x,moy_rapport_px_y
      
    def dans_le_cercle(self,x,y):
        
        if (self.i==0):
            return (x >= 347 and x<= 370)and (y >= 264 and y<= 311)
        elif (self.i == 1 ):
            return (x >= 311 and x<= 359)and (y >= 265 and y<= 314)
        elif (self.i == 2 ):
            return (x >= 301 and x<= 360)and (y >= 282 and y<= 321)
        elif (self.i == 3 ):
            return (x >= 331 and x<= 373)and (y >= 293 and y<= 324)
        else :
            return (x >= 322 and x<= 352)and (y >= 289 and y<= 325)

    def retablir_variable(self):
        self.tab_x= []
        self.tab_y= []
        self.p = 0
        self.i = self.i + 1
        
    def calcul_moy_rapport(self,x,y):
        self.tab_moy_rapport_x.append(x) 
        self.tab_moy_rapport_y.append(y) 
        
        a = int(sum(self.tab_moy_rapport_x)/len(self.tab_moy_rapport_x))
        b = int(sum(self.tab_moy_rapport_y)/len(self.tab_moy_rapport_y))
        
        return a,b
        
        
    def move(self,Window,Point,canvas):
        Ax,Ay,Bx,By = canvas.coords(Point.P)
        
        if ( Point.c==1):
            while (Bx != 0) :
                canvas.move(Point.P,-self.xinc,0)
                Ax,_,Bx,_ = canvas.coords(Point.P)
                self.Animation_Window.update()
                time.sleep(self.Refresh_Sec)
        elif(Point.c==0):
            while (Ax!= self.width + 20 ) :
                canvas.move(Point.P,self.xinc,0)
                Ax,_,_,_ = canvas.coords(Point.P)
                self.Animation_Window.update()
                time.sleep(self.Refresh_Sec)
        else:
            while (By!= 0 ) :
                canvas.move(Point.P,0,-self.yinc)
                _,_,_,By = canvas.coords(Point.P)
                self.Animation_Window.update()
                time.sleep(0.01)
                
    def calcul_du_rapport(self):
        if self.i == 0:
            return 0,0
        else :
            #calcul du rapport pour x
            a = abs(self.tab_xp_xe[1][self.i]-self.tab_xp_xe[1][self.i-1])
            b = abs(self.tab_xp_xe[0][self.i]-self.tab_xp_xe[0][self.i-1])
            
            rapport_px_x = int (b / a)
            
            #calcul du rapport pour y
            a = abs(self.tab_yp_ye[1][self.i]-self.tab_yp_ye[1][self.i-1])
            b = abs(self.tab_yp_ye[0][self.i]-self.tab_yp_ye[0][self.i-1])
            
            rapport_px_y = int (b / a)
            
            return  rapport_px_x,rapport_px_y
            

            
    def fix_point(self):
        print("dans la récupération du regard fix point")
        print(len(self.tab_x))
        return len(self.tab_x)>=self.nb_frames and len(self.tab_y)>=self.nb_frames
        
    def recuperation_x_y(self,x,y):
        self.tab_x.append(x)
        self.tab_y.append(y)
        
    def position_x_y_sur_ecran(self):
        self.tab_xp_xe[1][self.i] = int(sum(self.tab_x)/len(self.tab_x))
        self.tab_yp_ye[1][self.i] =int(sum(self.tab_y)/len(self.tab_y))
        
    def creation_points(self):
        if (self.i == 0):
            #point N1
            return Point(100,100,100+self.diam,100+self.diam,self.diam,self.Animation_canvas,1)
        elif self.i ==1 :
            #point N2
            (a,b)=(self.width-100, 100+self.diam)
            (a2,b2)=(a-self.diam, b-self.diam)
            return Point(a2,b2,a,b,self.diam,self.Animation_canvas,0)
        elif self.i == 2 :
            #point N3
            (a,b)=(self.width-100, self.height-100)
            (a2,b2)=(a-self.diam, b-self.diam)
            return Point(a2,b2,a,b,self.diam,self.Animation_canvas,0)
        elif self.i == 3 :
            #point N4
            (a2,b2)=(100, self.height-(100+self.diam))
            (a,b)=(a2+self.diam, b2+self.diam)
            return Point(a2,b2,a,b,self.diam,self.Animation_canvas,1)
        else :
            #point N5
            (a1,b1)=(int((self.width/2)),int((self.height/2)))
            (a,b)=(a1-int((self.diam/2)), b1-int((self.diam/2)))
            (a2,b2)=(a+self.diam, b+self.diam)
            return Point(a,b,a2,b2,self.diam,self.Animation_canvas,2)