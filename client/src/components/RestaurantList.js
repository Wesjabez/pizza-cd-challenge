import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RestaurantList = () => {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        axios.get('/restaurant')
            .then(response => {
                setRestaurants(response.data);
            })
            .catch(error => {
                console.error('Error fetching restaurants:', error);
            });
    }, []);

    return (
        <div>
            <h1>Restaurants</h1>
            <ul>
                {restaurants.map(restaurant => (
                    <li key={restaurant.id}>
                        <strong>{restaurant.name}</strong> - {restaurant.address}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RestaurantList;
