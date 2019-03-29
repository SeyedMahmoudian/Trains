"""
File name : Stop.py
Author : SeyedAmin SeyedMahmoudian

"""
class Stop:
    def __init__(self, station):
        """
        create stop Object.
        :param station:
        """
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
        """
        :return: name of the stop
        """
        return [s.name for s in self.connections()]