from sql_alchemy import database

class HotelModel(database.Model):
    __tablename__ = 'hotels' # O nome real da tabela no banco

    hotel_id = database.Column(database.String, primary_key = True)
    name = database.Column(database.String(80), nullable = False)
    star = database.Column(database.Float(precision=2, decimal_return_scale=1))
    price = database.Column(database.Float(precision=8, decimal_return_scale=2))
    city = database.Column(database.String)

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'star': self.star,
            'price': self.price,
            'city': self.city
        }
    
    def save_hotel(self):
        database.session.add(self)
        database.session.commit()

    def update_hotel(self, name, star, price, city):
        self.name = name
        self.star = star
        self.price = price
        self.city = city

        self.save_hotel()

    @classmethod
    def all_hotels(cls):
        hotels =  [hotel.json() for hotel in cls.query.all()]

        return hotels

    @classmethod
    def create_hotel(cls, hotel_id, name, star, price, city):
        hotel = cls(
            hotel_id = hotel_id,
            name = name,
            star = star,
            price = price,
            city = city
        )

        hotel.save_hotel()

        return hotel

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        
        return hotel