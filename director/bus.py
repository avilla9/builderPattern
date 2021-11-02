from builder.navigation_builder import NavigationBuilder


class BusDirector:

    def construct(origin, destiny):
        return NavigationBuilder()\
            .transportType("en Bus")\
            .originLocation(origin)\
            .destinyLocation(destiny)\
            .arrival(35)\
            .getInformation()
