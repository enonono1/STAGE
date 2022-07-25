import cv2
from gaze_tracking import GazeTracking

"""
programme qui vient retourner les coordonnées de la position des pupilles en x et y , c'est la position moyenne sur 150 frames.
"""

gaze = GazeTracking()

nb_frames = 150
tab_xd = []
tab_yd = []
tab_xg = []
tab_yg = []
tab_x= []
tab_y= []
i =0

def finish():

    return len(tab_xd) >= nb_frames and len(tab_yd) >= nb_frames and len(tab_xg) >= nb_frames and len(tab_yg) >= nb_frames

def valeurs():
    xd =int(sum(tab_xd) / len(tab_xd))
    yd =int(sum(tab_yd) / len(tab_yd))
    xg =int(sum(tab_xg) / len(tab_xg))
    yg =int(sum(tab_yg) / len(tab_yg))
    return xd,yd,xg,yg

def recuperartion_valeurs(xd,yd,xg,yg):
    tab_xd.append(xd)
    tab_yd.append(yd)
    tab_xg.append(xg)
    tab_yg.append(yg)
    
    
    
cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

while True:
    #ret obtient un indicateur de succès d'image
    ret, frame = cap.read()

    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    xg,yg = gaze.pupil_left_coords()
    xd,yd = gaze.pupil_right_coords()
    
    if (xg != None ) and (xd != None ) and (yg != None ) and (yd != None ):
        if not finish():
            print(xg,yg ,xd,yd)
            recuperartion_valeurs(xd,yd,xg,yg)
    
    #Afficher le cadre
    cv2.imshow('camera capture', frame)
    
    
    if finish():
        print("STOP")
        xd,yd,xg,yg = valeurs()
        print("position oeil droit")
        print("x :",xd)
        print("y :",yd)
        print("position oeil gauche")
        print("x :",xg)
        print("y :",yg)
        x = (xd+xg)/2
        y = (yd+yg)/2
        print("position moyenne de x et y")
        print(x,y)
    
    k = cv2.waitKey(1) #Attendez 1 ms
    if k == 27: #Quitter avec la touche ESC
        break

    
#Libérez la capture
cap.release()
cv2.destroyAllWindows()



    
