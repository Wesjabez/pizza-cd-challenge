from .config import db




class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    address = db.Column(db.String(255), nullable = False)
   
    restaurant_pizzas = db.relationship("RestaurantPizza",  back_populates="restaurant")
