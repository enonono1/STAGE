from threading import Thread
import cv2

class VideoShow:
    
    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
                cv2.imshow("Frame", self.frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
            
    def stop(self):
        self.stopped = True
        cv2.destroyAllWindows()
        
        
