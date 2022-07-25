import cv2
from gaze_tracking import GazeTracking
from fenetre_ecran import Fenetre_ecran
from calibration_ecran import Calibration_coordonne_vers_ecran
from suivi_ecran import suivi_ecran
from datetime import datetime

class CountsPerSec:
    """
    Class that tracks the number of occurrences ("counts") of an
    arbitrary event and returns the frequency in occurrences
    (counts) per second. The caller must increment the count.
    """

    def __init__(self):
        self._start_time = None
        self._num_occurrences = 0

    def start(self):
        self._start_time = datetime.now()
        return self

    def increment(self):
        self._num_occurrences += 1

    def countsPerSec(self):
        elapsed_time = (datetime.now() - self._start_time).total_seconds()
        return self._num_occurrences / elapsed_time if elapsed_time > 0 else 0

def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """
    print("{:.0f} iterations/sec".format(iterations_per_sec))
    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame

gaze = GazeTracking()
""" initialisation des fonctions pour créer une fenêtre avec tkinter """
ecran = Fenetre_ecran()

calibration_ecran = Calibration_coordonne_vers_ecran(ecran.Animation_canvas,ecran.Animation_Window,ecran.width,ecran.height)

cps = CountsPerSec().start()
i = 1
a =0

cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

while True:
    #ret obtient un indicateur de succès d'image
    ret, frame = cap.read()

    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    putIterationsPerSec(frame, cps.countsPerSec())
    
    x = gaze.coordonne_en_x_moy()
    y = gaze.coordonne_en_y_moy()
    
    print(x,y)
    #Afficher le cadre
    cv2.imshow('camera capture', frame)
    print(frame)
    
    if not calibration_ecran.calibration_point_termine():
         rapport_x,rapport_y = calibration_ecran.start_calibration(x,y)
    
    if a ==0:
        ecran2 = Fenetre_ecran()
        sv_ec = suivi_ecran(ecran2.Animation_canvas,ecran2.Animation_Window)
        a =1 
         
    sv_ec.start(x,y,rapport_x,rapport_y)
    #cv2.imshow("Demo", frame)
    
    k = cv2.waitKey(1) #Attendez 1 ms
    if k == 27: #Quitter avec la touche ESC
        break

    # Affichage de la fenêtre créée :
    ecran.Animation_Window.update()   
    i = i+ 1
    cps.increment()
    
#Libérez la capture
cap.release()
cv2.destroyAllWindows()

    
 

  