import sys
from NoSuchStation import NoSuchStation


class Station:
    def __init__(self, name):
        self.name = name
        self.distances_by_station = {}
        self.distance = sys.maxsize

    def add_connection(self, connection, dist=0):
        self.distances_by_station[connection] = dist

    def connections(self):
        return self.distances_by_station.keys()

    def connection_name(self):
        names = [station.name for station in self.connections()]
        return names

    def distance_to(self, connection):
        try:
            return self.distances_by_station[connection]
        except KeyError:
            raise NoSuchStation("No Such Route")

    def __str__(self):
        return ('<Station: ' + str(self.name) + ': ' +
                str([x.name for x in self.distances_by_station]) +
                '>')
