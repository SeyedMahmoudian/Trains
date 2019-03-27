class TripStop:
    def __init__(self, station):
        """create Station Object."""
        self.station = station
        self.name = station.name
        self.prevstop = None
        self.nextstop = None
        self.visited = False
        self.first = False
        self.last = False

    def connections(self):
        return self.station.connections()

    def connection_names(self):
        return [s.name for s in self.connections()]