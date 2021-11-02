from builder.navigation_builder import NavigationBuilder


class WalkDirector:

    def construct(origin, destiny):
        return NavigationBuilder()\
            .transportType("Caminando")\
            .originLocation(origin)\
            .destinyLocation(destiny)\
            .arrival(55)\
            .getInformation()
