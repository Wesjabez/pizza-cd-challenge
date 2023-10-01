import React, { useState } from 'react';
import axios from 'axios';

const RestaurantForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        address: ''
    });

    const handleInputChange = event => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = event => {
        event.preventDefault();
        axios.post('/restaurants', formData)
            .then(response => {
                console.log('Restaurant created successfully:', response.data);
                // Handle success, e.g., redirect to the restaurant detail page
            })
            .catch(error => {
                console.error('Error creating restaurant:', error);
            });
    };

    return (
        <div>
            <h1>Create Restaurant</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleInputChange} required />
                </div>
                <div>
                    <label>Address:</label>
                    <input type="text" name="address" value={formData.address} onChange={handleInputChange} required />
                </div>
                <button type="submit">Create Restaurant</button>
            </form>
        </div>
    );
};

export default RestaurantForm;
