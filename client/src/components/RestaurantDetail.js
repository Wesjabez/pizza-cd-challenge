import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RestaurantDetail = ({ match }) => {
    const [restaurant, setRestaurant] = useState(null);

    useEffect(() => {
        const restaurantId = match.params.id;
        axios.get(`/restaurants/${restaurantId}`)
            .then(response => {
                setRestaurant(response.data);
            })
            .catch(error => {
                console.error('Error fetching restaurant:', error);
            });
    }, [match.params.id]);

    if (!restaurant) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{restaurant.name}</h1>
            <p>Address: {restaurant.address}</p>
            <h2>Pizzas</h2>
            <ul>
                {restaurant.pizzas.map(pizza => (
                    <li key={pizza.id}>{pizza.name} - {pizza.ingredients}</li>
                ))}
            </ul>
        </div>
    );
};

export default RestaurantDetail;
