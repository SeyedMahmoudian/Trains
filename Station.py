import sys

"""
File name : Station.py
Author : SeyedAmin SeyedMahmoudian

"""
from NoSuchStation import NoSuchStation

class Station:
    def __init__(self, name):
        """
        create station object
        :param name: name of the station
        """
        self.name = name
        self.distances_by_station = {}
        self.distance = sys.maxsize

    def add_connection(self, connection, dist=0):
        """

        :param connection: add the connection
        :param dist: add the distance
        """
        self.distances_by_station[connection] = dist

    def connections(self):
        """
        :return: key of the distance of the station in array
        """
        return self.distances_by_station.keys()

    def connection_name(self):
        """
        :return: name of the station
        """
        names = [station.name for station in self.connections()]
        return names

    def distance_to(self, connection):
        """
        :param connection: Calculate the distance to the next connection and if there is no stop raise the no such
                           station
        :return: distance to the station
        """
        try:
            return self.distances_by_station[connection]
        except KeyError:
            raise NoSuchStation("No Such Route")

    def __str__(self):
        """

        :return: String for the station
        """
        return ('<Station: ' + str(self.name) + ': ' +
                str([x.name for x in self.distances_by_station]) +
                '>')
