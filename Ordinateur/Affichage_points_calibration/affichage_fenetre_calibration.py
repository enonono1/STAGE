from tkinter import *
from win32api import GetSystemMetrics 
import time


#################### VARIABLE GLOBAL #################
 
Width1 = GetSystemMetrics(0)
Height1 = GetSystemMetrics(1)

diam=40


Refresh_Sec = 0.01

xinc = yinc = 10

fixation_regard = 50

#################### Fonctions / class #################

def create_animation_window():
  Window = Tk()
  Window.title("Python Guides")
  Window.geometry(f'{Width1}x{Height1}')
  return Window
 

def create_animation_canvas(Window):
  canvas = Canvas(Window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas
      
def move(Window,Point,canvas):
    Ax,Ay,Bx,By = canvas.coords(Point.P)
    
    if ( Point.c==1):
        while (Bx != -20) :
            canvas.move(Point.P,-xinc,0)
            Ax,_,Bx,_ = canvas.coords(Point.P)
            print(Bx)
            Animation_Window.update()
            time.sleep(Refresh_Sec)
    elif(Point.c==0):
        while (Ax!= Width1 + 20 ) :
            canvas.move(Point.P,xinc,0)
            Ax,_,_,_ = canvas.coords(Point.P)
            print(Ax)
            Animation_Window.update()
            time.sleep(Refresh_Sec)
    else:
        while (By!= 0 ) :
            canvas.move(Point.P,0,-yinc)
            _,_,_,By = canvas.coords(Point.P)
            Animation_Window.update()
            time.sleep(0.01)
        
def fix():
    i = 0
    while (i != 10) :
        i=i+1
        Animation_Window.update()
        time.sleep(0.2)
    return True

class Point:
    def __init__(self, abs1, ord1,abs2, ord2,canvas,cote):
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

#################### MAIN #################

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)

#point N1
P1 = Point(100,100,100+diam,100+diam,Animation_canvas,1)

if(fix()):
    move(Animation_Window,P1,Animation_canvas)

#point N2
B=(a,b)=(Width1-100, 100+diam)
A=(a2,b2)=(a-diam, b-diam)

P2 = Point(a2,b2,a,b,Animation_canvas,0)

if(fix()):
    move(Animation_Window,P2,Animation_canvas)

#point 3
B=(a,b)=(Width1-100, Height1-100)
A=(a2,b2)=(a-diam, b-diam)
P3 = Point(a2,b2,a,b,Animation_canvas,0)
if(fix()):
    move(Animation_Window,P3,Animation_canvas)

#point N4
A=(a2,b2)=(100, Height1-(100+diam))
B=(a,b)=(a2+diam, b2+diam)
P4 = Point(a2,b2,a,b,Animation_canvas,1)
if(fix()):
    move(Animation_Window,P4,Animation_canvas)

#point N5
CA=(a1,b1)=(int((Width1/2)),int((Height1/2)))
A=(a,b)=(a1-int((diam/2)), b1-int((diam/2)))
B=(a2,b2)=(a+diam, b+diam)

P5 = Point(a,b,a2,b2,Animation_canvas,2)
if(fix()):
    move(Animation_Window,P5,Animation_canvas)

# Affichage de la fenêtre créée :
Animation_canvas.mainloop()