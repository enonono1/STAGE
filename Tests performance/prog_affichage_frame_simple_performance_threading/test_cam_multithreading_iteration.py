from pivideostream import VideoStream
from Show_video import VideoShow
from fps import FPS
import time


# démare thread stream video , show video
# démare le compteur
print("Start")
vs = VideoStream().start()
vs2= VideoShow(vs.frame).start()

time.sleep(2.0)

fps = FPS().start()
t = time.time()

while (time.time()-t)<20 :
    
    if vs.stopped or vs2.stopped:
        vs2.stop()
        vs.stop()
        break
    
    frame = vs.frame
    vs2.frame = frame
    fps.update()



fps.stop()

print("Temps écoulé: {:.2f}".format(fps.elapsed()))
print("Nombre de frame par seconde : {:.2f}".format(fps.fps()))


vs.stop()
vs2.stop()