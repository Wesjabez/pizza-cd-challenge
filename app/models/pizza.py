from .config import db
# from .restaurant_pizzas import RestaurantPizza




class Pizza(db.Model):
    
    id = db.Column(db.Integer ,primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    ingredients = db.Column(db.String(255), nullable = False)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates='pizza')