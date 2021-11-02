from builder.navigation_builder import NavigationBuilder

# Builder director constructor method to get done the product


class WalkDirector:

    def construct(origin, destiny):
        return NavigationBuilder()\
            .transportType("Caminando")\
            .originLocation(origin)\
            .destinyLocation(destiny)\
            .arrival(55)\
            .getInformation()
