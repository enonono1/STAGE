from threading import Thread
import cv2
class VideoStream:
    
    def __init__(self, src=cv2.CAP_DSHOW):
       self.stream = cv2.VideoCapture(src)
       (self.grabbed, self.frame) = self.stream.read()
       self.stopped = False

    def start(self):
        
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
            
    def stop(self):
        self.stopped = True
        
        
