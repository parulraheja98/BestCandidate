import React, { Component } from 'react'
import {Nav,Navbar} from 'react-bootstrap';
import '../App.css';
import {withRouter} from 'react-router-dom';

export class NavBar extends Component {


    constructor(props){
        super(props);
        this.state = {
            loggedIn : false,
            loginInfo : '',
            admin : false
        };
        this.logout = this.logout.bind(this);
    }


    logout(event) {
        console.log("Logged out!");
        //const {cookies} = this.props;
        //cookies.remove('loginCredentials' , {path:'/'});
        //this.props.history.push('/');
    
    }



    render() {
        return (
            <div>
               <Navbar bg="dark" variant="dark">
                    <Navbar.Brand href="/">Best Candidate</Navbar.Brand>
                    <Nav className="mr-auto">
                        {this.state.admin ?
                        <Nav.Link href="/adminpanel"> Admin Panel </Nav.Link>
                        : null}

                        {this.state.loggedIn ?
                        <Nav.Link onClick={this.logout}> Logout </Nav.Link>
                        : <Nav.Link onClick={this.login}> Login </Nav.Link>}

                        {this.state.loggedIn ?
                        null
                        : <Nav.Link href="/register"> Sign Up </Nav.Link>}    

                        <Nav.Link href="/about"> About </Nav.Link>
                    </Nav>
                </Navbar>  
            </div>
        )
    }
}

export default withRouter(NavBar);