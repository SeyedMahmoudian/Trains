import sys
from Station import Station
from Trip import Trip


class Rails:

    def __init__(self):
        self.stations_by_name = {}

    def add_station(self, name):
        self.stations_by_name[name] = Station(name)

    def add_rail(self, leave, arrive, distance=0):
        if leave not in self.stations_by_name:
            self.add_station(leave)
        if arrive not in self.stations_by_name:
            self.add_station(arrive)
        self.stations_by_name[leave].add_connection(self.stations_by_name[arrive], distance)


    def trip_for_stopnames(self, stopnames=[]):
        matching_stations = [self.stations_by_name[name] for name in stopnames]
        return Trip(matching_stations)

    def distance_for_trip(self, stopnames=[]):
        trip = self.trip_for_stopnames(stopnames)
        return trip.distance()

    def all_trips(self, tripnames, max_depth=0, max_stops=sys.maxsize, max_distance=sys.maxsize):
        if max_depth > 0:
            yield tripnames

            trip = self.trip_for_stopnames(tripnames)
            for x in trip.candidate_stop_names():
                for p in self.all_trips(tripnames + [x], max_depth - 1):
                    if len(p) <= max_stops:
                        newtrip = self.trip_for_stopnames(p)
                        if newtrip.distance() <= max_distance:
                            yield p

    def trip_from(self, name, max_depth=10, max_stops=30, max_distance=50):
        all_trip_names = self.all_trips([name], max_depth, max_stops, max_distance)
        return all_trip_names

    def trip_from_to(self, startname, targetname, max_depth=10, max_stops=30, max_distance=50):
        all_trip_names = self.trip_from(startname, max_depth, max_stops, max_distance)
        matching_trips = []
        for tripnames in all_trip_names:
            if len(tripnames) > 1:
                trip = self.trip_for_stopnames(tripnames)
                if trip.stops[-1].name == targetname:
                    matching_trips.append(trip)
        return matching_trips

    def trip_distance(self, trips):

        distance_trips = {}
        for t in trips:
            distance_trips[t.distance()] = t
        return distance_trips

    def trips_with_stops(self, startname, targetname, stops):
        trips = self.trip_from_to(startname, targetname, max_depth=15, max_stops=stops * 2)
        matching_trips = []
        for trip in trips:
            if trip.stops_count() == stops:
                matching_trips.append(trip)
        return matching_trips

    def trips_ordered_by_distance(self, trips):
        trips_dict = self.trip_distance(trips)
        ordered_distance = sorted(trips_dict.keys())
        for distance in ordered_distance:
            yield trips_dict[distance]

    def shortest_from_to(self, startname, targetname):
        all_trips = self.trip_from_to(startname, targetname, max_depth=15)
        ordered_trips = list(self.trips_ordered_by_distance(all_trips))
        return ordered_trips[0]

    def __str__(self):
        station_strings = ", ".join([str(station) for station in self.stations_by_name.values()])
        return str("<Railway: " + station_strings + ">")
