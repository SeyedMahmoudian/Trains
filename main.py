from Rails import Rails
from NoSuchStation import NoSuchStation
from NoSuchRoute import NoSuchRoute


def example():
    railsystem = Rails()
    railsystem.add_rail('A', 'B', 5)
    railsystem.add_rail('B', 'C', 4)
    railsystem.add_rail('C', 'D', 8)
    railsystem.add_rail('D', 'C', 8)
    railsystem.add_rail('D', 'E', 6)
    railsystem.add_rail('A', 'D', 5)
    railsystem.add_rail('C', 'E', 2)
    railsystem.add_rail('E', 'B', 3)
    railsystem.add_rail('A', 'E', 7)
    return railsystem


def example_trips():
    trips = [
        ['A', 'B', 'C'],
        ['A', 'D'],
        ['A', 'D', 'C'],
        ['A', 'E', 'B', 'C', 'D'],
        ['A', 'E', 'D']]
    return trips


def print_trip_distances(railsystem):
    trips = example_trips()
    for trip in trips:
        print("Output #%d: " % (trips.index(trip) + 1)),
        try:
            distance = railsystem.distance_for_trip(trip)
        except NoSuchStation:
            print("Surprise!")
        except NoSuchRoute:
            print("NO SUCH ROUTE")

        if distance:
            print("%d" % (distance))
        distance = 0


def print_trip_stops(railsystem):
    trips = railsystem.trip_from_to('C', 'C', max_stops=4)
    print("Output #6:  %d" % len(list(trips)))
    trips = railsystem.trips_with_stops('A', 'C', 4)
    print("Output #7:  %d" % len(list(trips)))


def print_shortest_trips(railsystem):
    a_to_c = railsystem.shortest_from_to('A', 'C')
    print("Output #8:  %d" % a_to_c.distance())
    b_to_b = railsystem.shortest_from_to('B', 'B')
    print("Output #9:  %d" % b_to_b.distance())


def print_distance_trips(railsystem):
    trips = railsystem.trip_from_to('C', 'C', max_distance=30 - 1)
    print("Output #10: %d" % len(list(trips)))


if __name__ == '__main__':
    """Call each of the sections to answer the ThoughtWorks problem."""
    railsystem = example()
    print_trip_distances(railsystem)
    print_trip_stops(railsystem)
    print_shortest_trips(railsystem)
    print_distance_trips(railsystem)
