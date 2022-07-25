import cv2
from gaze_tracking import GazeTracking
from Show_video import VideoShow
from video_get import VideoStream
from fps import FPS
import time

print("start")
vs = VideoStream().start()
vs2= VideoShow(vs.frame).start()

time.sleep(2.0)

fps = FPS().start()
t = time.time()
gaze = GazeTracking()

while (time.time()-t)<30 :
   
    frame = vs.frame
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    key = cv2.waitKey(1) & 0xFF

    vs2.frame = frame
    
    fps.update()
    
    if key == ord("q"):
        break


fps.stop()
print("Temps écoulé: {:.2f}".format(fps.elapsed()))
print("Nombre d'itération par seconde : {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()

