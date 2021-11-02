from builder.navigation_builder import NavigationBuilder

# Builder director constructor method to get done the product


class BusDirector:

    def construct(origin, destiny):
        return NavigationBuilder()\
            .transportType("en Bus")\
            .originLocation(origin)\
            .destinyLocation(destiny)\
            .arrival(35)\
            .getInformation()
