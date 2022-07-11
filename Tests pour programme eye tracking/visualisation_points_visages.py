import cv2
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

if not (cap.isOpened()):
    print("camera ne peut pas s'ouvrir")


while True:
    #ret obtient un indicateur de succès d'image
    ret, frame = cap.read()

    # si la frame est lu correctement alors ret = True
    if not ret:
        print("fin du stream, frame non reçu")
        break
    key = cv2.waitKey(1) & 0xFF

    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)


    faces = detector(gray)

    #pour chaque visage on vient récupérer des coordonnées des points que l'on veut (coordonnées pixel de l'image)
    for face in faces:
        x1 = face.left()
        y1 = face.top() 
        x2 = face.right()
        y2 = face.bottom()
    
    
        landmarks = predictor(image=gray, box=face)
        #le N 27 cordonnées du point entre les deux yeux.
        # x = landmarks.part(27).x
        #y = landmarks.part(27).y
    
        
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y

           
            cv2.circle(frame, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)

        cv2.circle(frame, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)
        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)
   
        cv2.imshow('frame', frame)
        if key == 27: #Quitter avec la touche ESC
            break


cv2.destroyAllWindows()
