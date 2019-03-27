from itertools import tee
from NoSuchRoute import NoSuchRoute
from TripStop import TripStop

class Trip:

    def __init__(self, stations=[]):
        """construct a list of railway station stops using station objects."""
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
        self.stops.append(TripStop(station))

    def segments(self):
        """return a list of pairs made of the steps of this trip."""
        starts, targets = tee(self.stops)
        next(targets, None)
        segments = zip(starts, targets)
        for start, target in segments:
            if target.name in start.connection_names():
                if start != target:
                    start.nextstop = target
                    target.prevstop = start
                    yield (start, target)
            else:
                raise NoSuchRoute()

    def distance(self):
        distances = []
        for start, target in self.segments():
            distances.append(start.station.distance_to(target.station))
        return sum(distances)

    def stops_count(self):
        """ThoughtWorks example lists a route of C-E-B-C as having three stops.
        Basically it excludes the starting point as a stop for our purposes.
        """
        return len(self.stops) - 1

    def candidate_stop_names(self, non_visited_only=False):
        """Given the last stop in this trip, return candidate stop names."""
        return self.stops[-1].connection_names()

    def stop_names(self):
        """Simple characters as expected by the ThoughtWorks problem."""
        return "-".join([s.name for s in self.stops])

    def __str__(self):
        return ('<' +
                str([s.name for s in self.stops]) +
                ' stops: ' + str(self.stops_count()) +
                ' distance: ' + str(self.distance()) +
                '>')
