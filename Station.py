import sys
import NoSuchStation
class Station:
    def __init__(self, name):
        self.name = name
        self.distance_by_station = {}
        self.distance = sys.maxsize

    def add_connection(self,connection,dist=0):
        self.distance_by_station[connection]=dist

    #Return instance of station
    def connecton(self):
        return self.distance_by_station.keys()

    def connection_names(self):
        names=[station.name for station in self.conneciton()]
        return names

    def distance_to(self,connection):
        try:
            return self.distance_by_station[connection]
        except KeyError:
            raise NoSuchStation("NO SUCH ROUTE")
    def __str__(self):
        return('<Station:'+str(self.name)+':'+str([x.name for x in self.distance_by_station])+'>')