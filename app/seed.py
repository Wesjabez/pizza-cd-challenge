from app import app, db
from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizzas import RestaurantPizza



def create_pizzas():
    pizzas_data = [
        {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
        {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
        {"name": "Vegetarian", "ingredients": "Dough, Tomato Sauce, Cheese, Vegetables"}
    ]

    for data in pizzas_data:
        pizza = Pizza(**data)
        db.session.add(pizza)

def create_restaurants():
    restaurants_data = [
        {"name": "Pizza Hut", "address": "123 Main St"},
        {"name": "Domino's", "address": "456 Elm St"},
        {"name": "Papa John's", "address": "789 Oak St"}
    ]

    for data in restaurants_data:
        restaurant = Restaurant(**data)
        db.session.add(restaurant)

def create_restaurant_pizzas():
    restaurant_pizzas_data = [
        {"restaurant_id": 1, "pizza_id": 1, "price": 10.99},
        {"restaurant_id": 1, "pizza_id": 2, "price": 12.99},
        {"restaurant_id": 2, "pizza_id": 2, "price": 11.99},
        {"restaurant_id": 3, "pizza_id": 3, "price": 10.49}
    ]

    for data in restaurant_pizzas_data:
        rp = RestaurantPizza(**data)
        db.session.add(rp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_pizzas()
        create_restaurants()
        create_restaurant_pizzas()

        db.session.commit()
