import sys
import Station
import Trip

class RailSystem:

    def __init__(self):
        self.station_by_name = {}

    def add_station(self, name):
        self.station_by_name[name] = Station(name)

    def add_rail(self, source, target, distance=0):
        if source not in self.station_by_name:
            self.add_station(source)
        if target not in self.station_by_name:
            self.add_station(target)

        self.station_by_name[source].add_connection(self.station_by_name[target], distance)

    def trip_for_stopnames(self, stopnames=[]):
        match = [self.station_by_name[name] for name in stopnames]
        return Trip(match)

    def distance_for_trip(self, stopnames=[]):
        trip = self.trip_for_stopnames(stopnames)
        return trip.distance()

    def find_all_trips(self, tripNames, max_dpt=0, max_stops=sys.maxsize, max_distance=sys.maxsize):
        if max_dpt > 0:
            yield tripNames
            trip = self.trip_for_stopnames(tripNames)
            for x in trip.candiate_stop_names():
                for z in self.find_all_trips(tripNames + [x], max_dpt - 1):
                    if len(z) <= max_stops:
                        newTrip = self.trip_for_stopnames(z)
                        if newTrip.distance <= max_distance:
                            yield z

    def find_trip_from(self, name, max_dpt=10, max_stop=30, max_distance=50):
        all_trip_names = self.find_all_trips([name], max_dpt, max_stop, max_distance)
        return all_trip_names

    def find_trips_from_to(self, start, target, max_dept=10, max_stops=30, max_distance=50):
        all_trips_name = self.find_trip_from(start, max_dept, max_stops, max_distance)
        matching = []
        for tripNames in all_trips_name:
            if len(tripNames) > 1:
                trip = self.trip_for_stopnames(tripNames)
                if trip.stops[-1].name == target:
                    matching.append(trip)
        return matching

    def trip_with_distance(self,trip):
        distance_trip={}
        for t in trip:
            distance_trip[t.distance()]=t
        return distance_trip

    def trips_with_stops(self, source, target, stops):
        trips = self.find_trips_from_to(source, target, max_depth=15, max_stops=stops * 2)
        matching = []
        for trip in trips:
            if trip.stops_count() == stops:
                matching.append(trip)
        return matching

    def trips_ordered_by_distance(self, trips):
        trips_dict = self.trips_with_distance(trips)
        ordered_distance = sorted(trips_dict.keys())
        for distance in ordered_distance:
            yield trips_dict[distance]

    def shortest_from_to(self, startname, targetname):
        all_trips = self.find_trips_from_to(startname, targetname, max_depth=15)
        ordered_trips = list(self.trips_ordered_by_distance(all_trips))
        return ordered_trips[0]

    def __str__(self):
        station_strings = ", ".join([str(station) for station in self.stations_by_name.values()])
        return str("<Railway: " + station_strings + ">")