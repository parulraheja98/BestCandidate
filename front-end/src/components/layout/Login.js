import React, { Component } from 'react'
import {Form, Button, Alert} from 'react-bootstrap'
import {withCookies, Cookies} from 'react-cookie';
import PropTypes from 'prop-types';

export class Login extends Component {


    constructor(props){
        super(props);
        const { cookies } = props;
        this.state = {
            loggedIn: false, 
            username: '', 
            password: '', 
            invalidCredentials: false,
            minInputLength:2
        };
    }


   // USE PROP TYPES AND DEFAULT PROPS

    validateForm(){
        return (this.state.username.length > this.state.minInputLength && this.state.password.length > this.state.minInputLength);
    }

    handleSubmit = event => {
        event.preventDefault();
        console.log("sending "+this.state.username+" and "+this.state.password);
        const {cookies} = this.props;
            
        fetch('http://localhost:5000/login' , {method:'POST',credentials:'include',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({
                username: this.state.username,
                password: this.state.password
            })
            })
            .then(response => response.json()) 
            .then(response => {
            console.log(response);
            console.log('received response');
            if(response.access_token) {
                this.setState({invalidCredentials:false});
                cookies.set('access_token',response.access_token,{path:'/'}); //store the received tokens
                cookies.set('refresh_token', response.refresh_token, {path: '/'});
                this.setState({loggedIn:true});
                //this.props.history.push('/');
            }else {
                this.setState({invalidCredentials:true}); //show the notification that says invalid password
            }
            })   
    }

    

    handleChange = event => {
        console.log(event.target.id+"updating to "+event.target.value);
        this.setState({
          [event.target.id]: event.target.value
        });
      }
    


    render() {
        return (
            <div style={this.getLoginDivStyle()}>
                <h2>Welcome back, {this.props.title}</h2> 
                <br/>
               <Form style={this.getFormStyle()} onSubmit={this.handleSubmit}>
                    <Form.Group controlId="username">
                        <Form.Control autoFocus type='text' value={this.username} placeholder='Enter username' onChange={this.handleChange} required/>
                    </Form.Group>
                    <Form.Group controlId="password">
                        <Form.Control type="password" value ={this.password} onChange={this.handleChange} placeholder="Password" required/>
                    </Form.Group>
                    <br/>
                    <Button block  variant="primary" disabled={!this.validateForm()} type="submit">Login</Button>
                </Form>
                { this.state.invalidCredentials ?<Alert style={this.getAlertStyle()} variant='danger'>Failed to log in</Alert> :null}
                {this.state.loggedIn ?<Alert variant='success'>You are logged in</Alert>:null}
            </div>
        )
    }



    getAlertStyle = () => {
        return {
            margin: "auto",
            width: "50%",
            textAlign: "centered"
        }
    }


    getLoginDivStyle = () => {
        return {
            margin: "auto",
            width: "50%",
            borderStyle: "ridge",
            padding: '30px',
            marginTop: '50px',
            background: 'rgb(236, 234, 234)'
           
        }   
    }

    getFormStyle = () => {
        return {
            marginRight: "20px"
        }
    }
}

export default withCookies(Login)
