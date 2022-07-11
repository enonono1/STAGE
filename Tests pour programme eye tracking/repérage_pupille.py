import cv2
import dlib
import numpy as np

"""
but du programme : 
    repère les pupilles puis on peut avec la trackbar faire évoluer le seuil pour répérer les pupilles
"""



########################################################
#                    Definitions

def shape_to_np(shape, dtype="int"):
    # initialise (x,y) coordonées
    coords = np.zeros((68, 2), dtype=dtype)
    # boucle des 68 points du visages puis les convertis
    # vers un (x,y) coordonnées
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

def eye_on_mask(mask, side):

   points = [shape[i] for i in side]
   points = np.array(points, dtype=np.int32)
   mask = cv2.fillConvexPoly(mask, points, 255)
   return mask

def contouring(thresh, mid, img, right=False):
   cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
   try:
       cnt = max(cnts, key = cv2.contourArea)
       M = cv2.moments(cnt)
       cx = int(M['m10']/M['m00'])
       cy = int(M['m01']/M['m00'])
       if right:
           cx += mid
       cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
   except:
       pass
    
def nothing(x):
   pass


##############################################################################


cap = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

if not (cap.isOpened()):
    print("camera ne peut pas s'ouvrir")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

cv2.namedWindow('image1')
cv2.createTrackbar('threshold', 'image1', 0, 255, nothing)



while True:
    #ret obtient un indicateur de succès d'image
    ret, frame = cap.read()

    # si la frame est lu correctement alors ret = True
    if not ret:
        print("fin du stream, frame non reçu")
        break
       
    thresh = frame.copy()
    kernel = np.ones((9, 9), np.uint8)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray)

    for rect in rects:
        
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, left)
        mask = eye_on_mask(mask, right)
        mask = cv2.dilate(mask, kernel, 5)
        eyes = cv2.bitwise_and(frame, frame, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        mid = (shape[42][0] + shape[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
        threshold = cv2.getTrackbarPos('threshold', 'image1')
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1
        thresh = cv2.dilate(thresh, None, iterations=4) #2
        thresh = cv2.medianBlur(thresh, 3) #3
        thresh = cv2.bitwise_not(thresh)
        contouring(thresh[:, 0:mid], mid, frame)
        contouring(thresh[:, mid:], mid, frame, True)

        for (x, y) in shape[36:48]:
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)
            
        # montre image avec the face detections + facial landmarks
        cv2.imshow('eyes', frame)
        cv2.imshow("image", thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
