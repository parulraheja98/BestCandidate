import React, { Component } from 'react'
import {Form, Button, Alert} from 'react-bootstrap'

export class Login extends Component {


    constructor(props){
        super(props);
        const { cookies } = props;
        this.state = {loggedIn: false, username: '', password: '', invalidCredentials: false};
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleEmailInput = this.handleEmailInput.bind(this);
        this.handlePasswordInput = this.handlePasswordInput.bind(this);
    }

    handleSubmit(event) {

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
        .then(data => {
        console.log(data);
        console.log('received response');
        if(data.access_token) {
            this.setState({invalidCredentials:false});
            cookies.set('accessToken',data.access_token,{path:'/'}); //store the received tokens
            cookies.set('refreshToken', data.refresh_token, {path: '/'});
            this.setState({loggedIn:true});
            this.props.history.push('/');
        }else {
            this.setState({invalidCredentials:true}); //show the notification that says invalid password
        }
        })
        
    }

    handleEmailInput(event){
        event.preventDefault();
        this.setState({username : event.target.value});
        console.log(event.target.value);
    }

    handlePasswordInput(event){
        event.preventDefault();
        this.setState({username : event.target.value});
        console.log("Something going in the password");
    }


    render() {
        return (
            <div style={this.getLoginDivStyle()}>
                <h2>Login</h2> 
                <br/>
               <Form style={this.getFormStyle()}>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Control type="email" onClick={this.handleEmailInput} placeholder="Email"/>
                        <Form.Text className="text-muted"> We'll never share your email with anyone else. </Form.Text>
                    </Form.Group>
                    <Form.Group controlId="formBasicPassword">
                        <Form.Control type="password" onClick={this.handlePasswordInput} placeholder="Password" />
                    </Form.Group>
                    <br/>
                    <Button variant="primary"  onClick={this.handleSubmit} type="submit">Submit</Button>
                </Form>
                {
                this.state.invalidCredentials ?
                <Alert variant='danger'> Invalid Login Credentials </Alert>
                :null
                }
                {
                this.state.loggedIn ?
                <Alert variant='success'> You are logged in </Alert>
                :null
                }
            </div>
        )
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

export default Login
