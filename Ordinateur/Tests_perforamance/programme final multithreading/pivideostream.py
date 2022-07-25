# import the necessary packages
from threading import Thread
import cv2
class PiVideoStream:
    
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
                print(self.stream.read())
                (self.grabbed, self.frame) = self.stream.read()
                print(self.stream.read())
    def read(self):
        # return the frame most recently read
        return self.frame
            
    def stop(self):
        self.stopped = True
        
        