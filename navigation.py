class Navigation(): 

    def __init__(
        self,
        transport="Transportation method",
        origin="Current location",
        destiny="Desired location",
        arrival=0
    ):
        # car, walking or bus
        self.transport = transport
        # Colonia Nápoles, El Ángel de la Independencia
        self.origin = origin
        self.destiny = destiny
        # 10, 20, 30 or any time in minutes
        self.arrival = arrival

    def construction(self):  # Returns a string describing the journey

        return f"La ruta más rápida {self.transport} "\
            f"desde {self.origin} hasta {self.destiny}, "\
            f"le tomará {self.arrival} minutos."
