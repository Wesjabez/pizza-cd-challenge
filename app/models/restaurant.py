from .config import db
# from .restaurant_pizzas import RestaurantPizza



class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    address = db.Column(db.String(255), nullable = False)
    # restaurant_pizzas = db.relationship("RestaurantPizza" , backref = "restaurant" )
    restaurant_pizzas = db.relationship("RestaurantPizza",  back_populates="restaurant")
