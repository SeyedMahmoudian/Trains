import RailSystem, NoSuchRoute,NoSuchStation

def railsystem():
    railSystem = RailSystem()

    railSystem.add_rail('A','B',5)
    railSystem.add_rail('B', 'C', 4)
    railSystem.add_rail('C', 'D', 8)
    railSystem.add_rail('D', 'C', 8)
    railSystem.add_rail('D', 'E', 6)
    railSystem.add_rail('A', 'D', 5)
    railSystem.add_rail('C', 'E', 2)
    railSystem.add_rail('E', 'B', 3)
    railSystem.add_rail('A', 'E', 7)

    return railSystem

def trips():
    trips=[
        ['A','B','C'],
        ['A', 'D'],
        ['A', 'D', 'C'],
        ['A', 'E', 'B','C','D'],
        ['A', 'E', 'D']]
    return trips

def print_distance(railsystem):
    trip=trips()

    for t in trip:
        print("Output #%d",(trip.index(t) + 1), end=' ')
        try:
            distance = railsystem.distance_for_trip(t)
        except NoSuchStation:
            print("Stations does not exist!")
        except NoSuchRoute:
            print ("NO SUCH ROUTE")

        if distance:
            print("%d", (distance))
        distance=0

def print_stop(railsystem):
    trips=railsystem.find_trips_from_to('C','C',max_stops=4)
    print("Output #6: %d", len(list(trips)))
    trips=railsystem.trips_with_stops('A','C',4)
    print("Output #7: %d", len(list(trips)))

def print_short_trip(railsystem):
    a_to_c = railsystem.shortest_from_to('A', 'C')
    print
    "Output #8:  %d" % a_to_c.distance()
    b_to_b = railsystem.shortest_from_to('B', 'B')
    print
    "Output #9:  %d" % b_to_b.distance()


def print_distance_trips(railsystem):
    trips = railsystem.find_trips_from_to('C', 'C', max_distance=30 - 1)
    print
    "Output #10: %d" % len(list(trips))

if __name__ == '__main__':
    """Call each of the sections to answer the ThoughtWorks problem."""
    railsystem = railsystem()
    print_distance(railsystem)
    print_stop(railsystem)
    print_short_trip(railsystem)
    print_distance_trips(railsystem)