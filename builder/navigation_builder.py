from .journey_builder import JourneyBuilder
from navigation import Navigation


class NavigationBuilder(JourneyBuilder):

    def __init__(self):
        self.navigation = Navigation()

    def transportType(self, transport):
        self.navigation.transport = transport
        return self

    def originLocation(self, origin):
        self.navigation.origin = origin
        return self

    def destinyLocation(self, destiny):
        self.navigation.destiny = destiny
        return self

    def arrival(self, arrival):
        self.navigation.arrival = arrival
        return self

    def getInformation(self):
        return self.navigation
