from sql_alchemy import database

class HotelModel(database.Model):
    __tablename__ = 'hoteis' # O nome real da tabela no banco

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
    
