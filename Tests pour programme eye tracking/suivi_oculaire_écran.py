import tkinter as tk 
from win32api import GetSystemMetrics 
import time

"""
BUT du programme :
    simuler un suivi du regard avec des données déjà rentrées
    le programme sera réutilisé dans un programme de eye tracking pour la partie afficher le suivi du regard sur l'écran'*
"""





#################### VARIABLES #################
 
Width1 = GetSystemMetrics(0)
Height1 = GetSystemMetrics(1)

diam = 20
 
Tab =  [[59,58], [708, 50], [1209, 57], [1705, 58], [1705, 502], [1707, 708], [1200, 700], [1000, 700], [1000, 500], [1000, 250], [700, 250], [50, 250]]


#################### Fonctions / class #################

def create_animation_window():
  Window = tk.Tk()
  Window.title("fenêtre suivi pupille")
  Window.geometry(f'{Width1}x{Height1}')
  return Window
 

def create_animation_dessin(Window):
  dessin = tk.Canvas(Window)
  dessin.configure(bg="black")
  dessin.pack(fill="both", expand=True)
  return dessin

def move(canvas, Point):

    i = 0
    diam = 20 
    Ax,Ay = 0,0
    
    while i != 12 :

        position_oeil_x = round_to_decimal(Tab[i][0])
        position_oeil_y = round_to_decimal(Tab[i][1])

        Ax,Ay,_,_ = canvas.coords(Point)

        
        position_x_dessin = Ax + diam / 2
        position_y_dessin= Ay + diam / 2

        
        ecart_x =int( position_x_dessin - position_oeil_x)
        ecart_y = int(position_y_dessin - position_oeil_y)

        
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

        
        while (position_x_dessin != position_oeil_x )or(position_y_dessin != position_oeil_y ):
            xinc =5*Deplacment_x
            yinc =5*Deplacment_y
            

            canvas.move(Point,xinc,yinc)
  
            Ax,Ay,_,_ = canvas.coords(Point)

            position_x_dessin = Ax + diam / 2
            position_y_dessin= Ay + diam / 2

            Animation_Window.update()
            
        time.sleep(1)
        i = i + 1
        
def round_to_decimal(n):  
    return (int(n/10))*10


#################### MAIN #################

Animation_Window = create_animation_window()
Animation_dessin = create_animation_dessin(Animation_Window)

Ax,Ay,Bx,By = 0,0,30,30
Point=Animation_dessin.create_oval((Ax,Ay),(Bx,By), fill= 'red',outline='red', width=2)


move(Animation_dessin,Point)



# Affichage de la fenêtre créée :
Animation_dessin.mainloop()
