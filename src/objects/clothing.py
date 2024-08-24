class ClothingEntry:
    def __init__(self, brand_name, clothing_type, thumbnail_path, date_bought, wear_count, date_removed):
        self.brand_name = brand_name
        self.clothing_type = clothing_type
        self.thumbnail_path = thumbnail_path
        self.date_bought = date_bought
        self.wear_count = wear_count
        self.date_removed = date_removed

    def __str__(self):
        return f"""
        Clothing Entry Details
        Brand name: {self.brand_name}
        Clothing type: {self.clothing_type}
        Thumbnail path: {self.thumbnail_path}
        Date bought: {self.date_bought}
        Wear count (since Feb '24): {self.wear_count}
        Date removed: {self.date_removed}
        """