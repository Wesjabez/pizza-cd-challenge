# from .config import db
# from .restaurant import Restaurant



# class RestaurantPizza(db.Model):
#     id = db.Column(db.Integer, primary_key =  True)
#     price = db.Column(db.Float, nullable = False )
#     restaurant_id = db.Column(db.Integer, db.ForeignKey ("restaurant_id"),nullable = False )
#     pizza_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable = False)

#     pizza = db.relationship('Pizza', back_populates='pizza')
#     restaurant = db.relationship('Restaurant') 


from .config import db
from .pizza import Pizza

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas', uselist=False)
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    # restaurant_pizzas = db.relationship("RestaurantPizza" , backref = "restaurant" )
    # restaurant_pizzas = db.relationship("RestaurantPizza", back_populates='pizza')
