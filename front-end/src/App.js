import React, { Component } from 'react';
import {Switch,Route} from 'react-router';
import {BrowserRouter} from 'react-router-dom';
import './App.css';
import { NavBar } from './layout/NavBar';
import About from './layout/About';
import Login from './layout/Login';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <div>
        <NavBar />
        <Switch>
          <Route exact path='/' component={Login}/>
        </Switch>
        <Route path="/about" component={About}/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
