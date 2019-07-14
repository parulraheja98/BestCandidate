import React, { Component } from 'react';
import {Switch,Route} from 'react-router';
import {BrowserRouter} from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import { NavBar } from './layout/NavBar';
import About from './layout/About';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <div>
        <NavBar />
        <Switch>
          {/* <Route exact path='/' component={Login} />
          <Route exact path='/Register' component={Register} /> */}
        </Switch>
        <Route path="/about" component={About}/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
