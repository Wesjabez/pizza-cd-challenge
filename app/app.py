from models.config import db
from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.pizza import db as pizza_db, Pizza
from models.restaurant import db as restaurant_db, Restaurant
from models.restaurant_pizzas import db as rp_db, RestaurantPizza
from flask_cors import CORS

# from models.pizza import  Pizza
# from models.restaurant import Restaurant
# from models.restaurant_pizzas import RestaurantPizza


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///pizza_restaurant.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
db.init_app(app)




@app.route("/")
def home ():
    return ""

@app.route("/restaurants" , methods = ["GET"])
def get_restaurants():
    restaurants =  Restaurant.querry.all()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_data = {
            "id ": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.adress
        }
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)

@app.route("/restaurants/<int:restaurnt_id>", methods = ["GET"])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.querry.get(restaurant_id)
    if restaurant:
        pizzas = []
        for rp in restaurant.restaurant_pizzas:
            pizza_data = {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            }
            pizza.append(pizza_data)
            restaurant_data = {
                "id": restaurant.id,
                "name":restaurat.name,
                "address":restaurant.name,
                "pizza":pizzas
            }

            return  jsonify(restaurant_data)
    else:
                return jsonify({"error:restaurant id not found"}), 404


app.route("/restaurants/<int:restaurant_id>", methods = ["DELETE"])
def delete_restaurant(restauraunt_id):
    restaurant = Restaurant.querry.get(restaurant_id)
    if restaurant:
        RestaurantPizza.querry.filter(restaurant_id = restaurant.id).delete()
        restaurant_db.session.delete(restaurant)
        restaurant_db.session.commit.commit()
        return "", 204
    else:
        return jsonify({"error: restaurant id not found"}), 404

app.route("/pizzas", methods = ["GET"])
def get_pizzas():
    pizzas = Pizzas.querry.all()
    pizza_list = []
    for pizza in pizzas:
        pizza_data = {
            "id ":pizza.id,
            "name":pizza.name,
            "ingredients":pizza.ingredients
        }
        pizza_list.append(pizza_data)

    return jsonify(pizza_list)

@app.route("/restaurant_pizzas", methods = ["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = restaurant.get('restaurant_id')

    if not(price and pizza_id and restaurant_id):
        return jsoify({"errors": ["validation errors"]}), 400
    
    pizza =  Pizza.querry.get(pizza_id)
    restaurant = Restaurant.querry.get(restaurant_id)

    if pizza and restaurant:
        new_rp = RestaurantPizza(price = price, pizza_id= pizza_id, resauarnt_id = restaurant_id )
        rp_db.session.add(new_rp)
        rp_db.session.commit()

        return jsonify({
            "id":pizza.id, 
            "name":pizza.name,
            "ingredient":pizza.ingredients
        }), 201
    else:
        return jsonify({"errors": ["validation errors"]}),400
    

if __name__ == "__main__":
    app.run(debug = True, port = 5555)