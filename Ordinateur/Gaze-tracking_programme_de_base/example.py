"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking



gaze = GazeTracking()

#webcam = cv2.VideoCapture('A.mp4')
webcam = cv2.VideoCapture(0) #0 est le numéro de périphérique de la caméra

while True:
    # We get a new frame from the webcam
    a, frame = webcam.read()
    cv2.imshow("Frame", frame)
    
    if a is False:
        break
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    #calibration.debut()
    
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
        print("blink")
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    print(left_pupil)
    print(right_pupil)
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
