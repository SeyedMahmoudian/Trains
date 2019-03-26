import sys

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

    def find_all_trips(self, tripNames, max_dpt=0, max_stops=sys.maxsize, max_distance=sys.maxsize):
        if max_dpt>0:
            yield tripNames
            trip=self.trip_for_stopnames(tripNames)
            for x in trip.candiate_stop_names():
                for z in self.find_all_trips(tripNames + [x], max_dpt - 1):
                    if len(z) <= max_stops:
                        newTrip=self.trip_for_stopnames(z)
                        if newTrip.distance <= max_distance:
                            yield z


    def find_trip_from(self,name,max_dpt=10,max_stop=30,max_distance=50):
        all_trip_names=self.find_all_trips([name],max_dpt,max_stop,max_distance)
        return all_trip_names

