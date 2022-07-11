import cv2
from gaze_tracking import GazeTracking
from datetime import datetime
from fps import FPS
import time


fps = FPS().start()
t = time.time()

gaze = GazeTracking()

cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

    
while (time.time()-t)<30:
    
    
    #ret obtient un indicateur de succès d'image
    ret, frame = cap.read()
    
    key = cv2.waitKey(1)
    gaze.refresh(frame)
    
    frame = gaze.annotated_frame()
    
    cv2.imshow("Demo", frame)
    
    fps.update()
    
    k = cv2.waitKey(1) #Attendez 1 ms
    if k == 27: #Quitter avec la touche ESC
        break

fps.stop()
print("Temps écoulé: {:.2f}".format(fps.elapsed()))
print("Nombre de frame par seconde : {:.2f}".format(fps.fps()))

#Libérez la capture
cap.release()
cv2.destroyAllWindows()
