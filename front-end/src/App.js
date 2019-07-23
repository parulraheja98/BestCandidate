import React, { Component } from 'react';
import {Switch,Route} from 'react-router';
import {BrowserRouter} from 'react-router-dom';
import './App.css';
import { NavBar } from './components/layout/NavBar';
import About from './components/layout/About';
import Login from './components/layout/Login';
import Register from './components/layout/Register';
import LandingPage from './components/layout/LandingPage';
import Candidate from './components/Candidate';

class App extends Component {


  state = {
    role : "",
    loggedIn : false
  }

  render() {
    return (
      <BrowserRouter>
      <div>
        <NavBar />
        <Switch>
        <Route exact path="/about" component={About}/>
        <Route exact path="/recruiter-login" render={(props) => <Login {...props} title="Recruiter" />}/>
        <Route exact path="/candidate-login" render={(props) => <Login {...props} title="Candidate" />}/>
        <Route exact path="/" component={LandingPage}/>
        <Route exact path="/register" component={Register}/>
        <Route exact path="/candidate" component={Candidate}/>
        </Switch>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;
