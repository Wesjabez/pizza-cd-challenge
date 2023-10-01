import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RestaurantList from './components/RestaurantList';
import RestaurantDetail from './components/RestaurantDetail';
import PizzaList from './components/PizzaList';
import RestaurantForm from './components/RestaurantForm';

const App = () => {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/" exact component={RestaurantList} />
                    <Route path="/restaurants/:id" component={RestaurantDetail} />
                    <Route path="/pizzas" component={PizzaList} />
                    <Route path="/create" component={RestaurantForm} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;
