class ClothingItem:
    def __init__(self, brand, colour, type, thumbnail_path):
        self.brand = brand
        self.colour = colour
        self.type = type
        self.thumbnail_path = thumbnail_path

    def __str__(self):
        return f"""
        Clothing Item Details
        Brand: {self.brand}
        Colour: {self.colour}
        Type: {self.type}
        Thumbnail path: {self.thumbnail_path}
        """