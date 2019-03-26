class TripStop:
    def __init__(self,station):
        self.station=station
        self.name=station.name
        self.prevStop=None
        self.nextStop=None
        self.visitd=None
        self.first=None
        self.last=None

    def connection(self):
        return self.station.connections()

    def connections(self):
        return self.station.connections()

    def connecition_names(self):
        return [n.name for n in self.connections()]