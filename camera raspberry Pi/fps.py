import datetime

class FPS:
    
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0
        
    def start(self):
        # start timer
        self._start = datetime.datetime.now()
        return self
    
    def stop(self):
        # stop timer
        self._end = datetime.datetime.now()
        
    def update(self):
        # augmente le nombre de frame durant start et stop
        self._numFrames += 1
        
    def elapsed(self):
        #nombre de seconde écoulé
        return (self._end - self._start).total_seconds()
    
    def fps(self):
        # retourne frames/seconde
        return self._numFrames / self.elapsed()