from itertools import tee
from NoSuchRoute import NoSuchRoute
from Stop import Stop


class Trip:

    def __init__(self, stations=[]):
        self.stops = []
        if stations:
            for s in stations:
                self.add_stop(s)
        for s in self.stops:
            stopindex = self.stops.index(s)
            if stopindex == 0:
                s.first = True
            elif stopindex == (len(self.stops) - 1):
                s.last = True

    def add_stop(self, station):
        self.stops.append(Stop(station))

    def segments(self):
        starts, end = tee(self.stops)
        next(end, None)
        segments = zip(starts, end)
        for start, target in segments:
            if target.name in start.connection_names():
                if start != target:
                    start.next = target
                    target.prev = start
                    yield (start, target)
            else:
                raise NoSuchRoute()

    def distance(self):
        distances = []
        for start, target in self.segments():
            distances.append(start.station.distance_to(target.station))
        return sum(distances)

    def stops_count(self):

        return len(self.stops) - 1

    def candidate_stop_names(self, non_visited_only=False):
        return self.stops[-1].connection_names()

    def stop_names(self):
        return "-".join([s.name for s in self.stops])

    def __str__(self):
        return ('<' +
                str([s.name for s in self.stops]) +
                ' stops: ' + str(self.stops_count()) +
                ' distance: ' + str(self.distance()) +
                '>')
