import Station
import Trip

class RailSystem:

    def __init__(self):
        self.station_by_name={}

    def add_station(self,name):
        self.station_by_name[name]=Station(name)

    def add_rail(self,source,target,distance=0):
        if source not in self.station_by_name:
            self.add_station(source)
        if target not in self.station_by_name:
            self.add_station(target)

        self.station_by_name[source].add_connection(self.station_by_name[target],distance)

    def trip_for_stopnames(self,stopnames=[]):
        match=[self.station_by_name[name] for name in stopnames]
        return Trip(match)

    def distance_for_trip(self, stopnames=[]):
        trip=self.trip_for_stopnames(stopnames)
        return trip.distance()