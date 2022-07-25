# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:04:35 2022

@author: enora
"""
import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    #Capturez la caméra
    cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

    while True:
        #ret obtient un indicateur de succès d'image
        ret, frame = cap.read()
        #Si ça ressemble à un miroir
        if mirror is True:
            frame = frame[:,::-1]

        #Redimensionner le cadre
        #la taille est, par exemple(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        #Afficher le cadre
        cv2.imshow('camera capture', frame)
        
        k = cv2.waitKey(1) #Attendez 1 ms
        if k == 27: #Quitter avec la touche ESC
            break

    #Libérez la capture
    cap.release()
    cv2.destroyAllWindows()
    
capture_camera()