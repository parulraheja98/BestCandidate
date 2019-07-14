import React, { Component } from 'react';
import {Switch,Route} from 'react-router';
import {BrowserRouter} from 'react-router-dom';
import './App.css';
import { NavBar } from './layout/NavBar';
import About from './layout/About';
import Login from './layout/Login';
import Register from './layout/Register';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <div>
        <NavBar />
        <Switch>
        <Route exact path="/about" component={About}/>
        <Route exact path="/login" component={Login}/>
        <Route exact path="/" component={Login}/>
        <Route exact path="/register" component={Register}/>
        </Switch>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;
