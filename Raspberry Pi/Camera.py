from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialisation des paramètres pour la capture
camera = PiCamera()
camera.resolution = (800, 600)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(800, 600))

# capture du flux vidéo
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # recupère à l'aide de Numpy le cadre de l'image, pour l'afficher ensuite à l'écran
    image = frame.array
    # affichage du flux vidéo
    key = cv2.waitKey(1) & 0xFF
    # initialisation du flux 
    rawCapture.truncate(0)
             
    cv2.imshow("Demo", image)

    # si la touche q du clavier est appuyée, on sort de la boucle
    if key == ord("q"):
        break

"""
import time
import picamera

camera = picamera.PiCamera()

try :
    camera.start_preview()
    #camera.start_recording('/home/pi/programme récupération données pour raspberry')
    camera.brightness=60
    time.sleep(5)
    #camera.stop_recording()
    camera.stop_preview()
  
finally :
    camera.close()
    
    
"""
