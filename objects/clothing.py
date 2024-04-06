class clothing_item:
    def __init__(self, brand, colour, type):
        self.brand = brand
        self.colour = colour
        self.type = type

    def __str__(self):
        return f"""
        Clothing Item Details
        Brand: {self.brand}
        Colour: {self.colour}
        Type: {self.type}
        """