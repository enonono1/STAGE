import cv2
from gaze_tracking import GazeTracking
from fenetre_ecran import Fenetre_ecran
from calibration_ecran import Calibration_coordonne_vers_ecran
from suivi_ecran import suivi_ecran
from pivideostream import PiVideoStream
from fps import FPS
import iterrations
import time

# created a *threaded *video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
cps = iterrations.CountsPerSec().start()
t = time.time()
gaze = GazeTracking(vs.get()).start()

""" initialisation des fonctions pour créer une fenêtre avec tkinter """
ecran = Fenetre_ecran()

calibration_ecran = Calibration_coordonne_vers_ecran(ecran.Animation_canvas,ecran.Animation_Window,ecran.width,ecran.height)

i = 1
a =0

# loop over some frames...this time using the threaded stream
while (time.time()-t)<30  :
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    print(frame)
    cv2.imshow("Frame", frame)
    time.sleep(5.0)
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    key = cv2.waitKey(1) & 0xFF
    # update the FPS counter
    iterrations.putIterationsPerSec(frame, cps.countsPerSec())
    #cv2.imshow("Frame", frame)
    
    x = gaze.coordonne_en_x_moy()
    y = gaze.coordonne_en_y_moy()
    
    print(x,y)

    
    if not calibration_ecran.calibration_point_termine():
         rapport_x,rapport_y = calibration_ecran.start_calibration(x,y)
    
    if a ==0:
        ecran2 = Fenetre_ecran()
        sv_ec = suivi_ecran(ecran2.Animation_canvas,ecran2.Animation_Window)
        a =1 
         
    sv_ec.start(x,y,rapport_x,rapport_y)
    # Affichage de la fenêtre créée :
    ecran.Animation_Window.update()
    
    i = i+ 1
    fps.update()
    cps.increment()
    if key == 27: #Quitter avec la touche ESC
        break


# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()