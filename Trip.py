from itertools import tee
from NoSuchRoute import NoSuchRoute
from TripStop import TripStop

class Trip:

    def __init__(self,stations=[]):
        self.stops=[]
        if stations:
            for s in stations:
                self.add_stop(s)
        for i in self.stops:
            index=self.stops.index(i)
            if index ==0:
                i.first=True
            elif index==(len(self.stops)-1):
                i.last=True

    def add_stop(self,station):
        self.stops.append(TripStop(station))

    def seg(self):
        start, target=tee(self.stops)
        next(target,None)
        seg=zip(start,target)
        for start,target in seg:
            if target.name in start.connection_names():
                if start != target:
                    start.nextstop=target
                    target.prevstop=start
                    yield(start,target)
                else:
                     raise NoSuchRoute()

    def distance(self):
        distances=[]
        for start , target in self.seg():
            distances.append(start.station.distance_to(target.station))
        return sum(distances)

    #First stop is not counted so remove one stop from the total number
    def stop_count(self):
        return len(self.stops)-1

    def candiate_stop_names(self,non_visited_only=False):
        return self.stops[-1].connection_names()

    def stop_names(self):
        return "-".join([s.name for s in self.stops])

    def __str__(self):
        return ('<'+
                str([s.name for s in self.stops])+
                'stops:'+str(self.stop_count())+
                'distance'+str(self.distance())+
                '>')
