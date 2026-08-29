class Product:
    def __init__(
        self,
        title: str,
        price: float,
        currency:str,
        available: bool,
        rating: int,
        source_url: str,
    ):
        self.title = title
        self.price = price
        self.currency = currency
        self.available = available
        self.rating = rating
        self.source_url = source_url