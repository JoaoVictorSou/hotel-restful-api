class HotelModel:
    def __init__(self, hotel_id, name, star, price, city):
        self.hotel_id = hotel_id
        self.name = name
        self.star = star
        self.price = price
        self.city = city
    
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'star': self.star,
            'price': self.price,
            'city': self.city
        }
