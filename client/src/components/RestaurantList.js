


import React, { useState, useEffect } from 'react';

const RestaurantList = () => {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/restaurants')
            .then(response => response.json())
            .then(data => {
                setRestaurants(data);
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
