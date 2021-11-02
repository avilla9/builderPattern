from abc import ABCMeta, abstractmethod


class JourneyBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def transportType(transport):
        "Transport type"

    @staticmethod
    @abstractmethod
    def originLocation(origin):
        "Origin location"

    @staticmethod
    @abstractmethod
    def destinyLocation(destiny):
        "Destiny location"

    @staticmethod
    @abstractmethod
    def arrival(arrival):
        "Arrival time"

    @staticmethod
    @abstractmethod
    def getInformation():
        "Return the whole journey information"
