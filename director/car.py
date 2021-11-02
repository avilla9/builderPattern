from builder.navigation_builder import NavigationBuilder


class CarDirector:

    def construct(origin, destiny):
        return NavigationBuilder()\
            .transportType("en Carro")\
            .originLocation(origin)\
            .destinyLocation(destiny)\
            .arrival(20)\
            .getInformation()
