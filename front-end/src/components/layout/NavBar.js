import React, { Component } from 'react'
import {Nav,Navbar} from 'react-bootstrap';
import '../../App.css';
import {withCookies, Cookies} from 'react-cookie';
import {withRouter, Redirect} from 'react-router-dom';

export class NavBar extends Component {


    constructor(props){
        super(props);
        this.state = {
            loggedIn : false,
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

    componentDidMount(){
        const {cookies} = this.props;
        if(cookies){
            if(cookies.get('access_token')) {
                console.log('(Nav bar) access token cookie exists, means we are logged in');
                this.setState({loggedIn:true});
            }else {
                console.log('(Nav Bar) not logged in');
                this.setState({loggedIn:false});
            }
        }    
    }



    render() {
        return (
            <div>
               <Navbar bg="dark" variant="dark">
                    <Navbar.Brand href="/">Best Candidate</Navbar.Brand>
                    <Nav className="mr-auto">
                        {this.state.admin ? <Nav.Link href="/admin-panel"> Admin Panel </Nav.Link>: null}
                        {this.state.loggedIn ? <Nav.Link onClick={this.logout}> Logout </Nav.Link> : <Nav.Link href="/recruiter-login"> Recruiter Login </Nav.Link>}
                        {this.state.loggedIn ? <Nav.Link onClick={this.logout}> Logout </Nav.Link> : <Nav.Link href="/candidate-login"> Candidate Login </Nav.Link>}
                        {this.state.loggedIn ? null: <Nav.Link href="/register"> Sign Up </Nav.Link>}    
                        <Nav.Link href="/about"> About </Nav.Link>
                    </Nav>
                </Navbar>  
            </div>
        )
    }
}

const NavigationBar = withCookies(NavBar);
export default withRouter(NavigationBar);