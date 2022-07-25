from fps import FPS
import cv2
import time

# démare thread stream video , show video
# démare le compteur
print("Start")

webcam = cv2.VideoCapture(0)

time.sleep(2.0)

fps = FPS().start()
t = time.time()

while (time.time()-t)<20 :
    
    #ret obtient un indicateur de succès d'image
    ret, frame = webcam.read()
   
    fps.update() 
        
    #Afficher le cadre
    cv2.imshow('camera capture', frame)
        
    k = cv2.waitKey(1) #Attendez 1 ms
    if k == 27: 
        #Quitter avec la touche ESC
        break

fps.stop()
print("Temps écoulé: {:.2f}".format(fps.elapsed()))
print("Nombre de frame par seconde : {:.2f}".format(fps.fps()))

#Libérez la capture
webcam.release()
cv2.destroyAllWindows()

