import React, { Component } from 'react'
import {Form, Button, Alert, ButtonGroup, ToggleButton} from 'react-bootstrap'


export class Register extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username:'',
            password:'',
            confPassword:'',
            email:'',
            credentialsMatch:true,
            role: ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleUsername = this.handleUsername.bind(this);
        this.handlePassword = this.handlePassword.bind(this);
        this.handleRePassword = this.handleRePassword.bind(this);
        this.handleEmail = this.handleEmail.bind(this);
        this.handleRole = this.handleRole.bind(this);
    }
    
    handleUsername(event) {
        event.preventDefault();
        this.setState({username:event.target.value});
    }
    
    handleEmail(event) {
        event.preventDefault();
        this.setState({email:event.target.value});
    }
    
    handlePassword(event) {
        event.preventDefault();
        this.setState({password:event.target.value});
    }
    
    handleRePassword(event) {
        event.preventDefault();
        this.setState({confPassword:event.target.value});
    }

    handleRole(event){
        event.preventDefault();
        console.log("this is the event");
        console.log(event);
    }

    handleSubmit(event) {

        event.preventDefault();
        console.log('checking username');
        console.log(this.state.username);
        console.log('checking usrname 1');
        
            var registerCredentials = JSON.stringify({
                username:this.state.username,
                password:this.state.password,
                role:this.state.role
            })
        
    
        fetch('http://localhost:5000/register' , {
        method:'POST',
        credentials:'include',
        headers:{'Content-Type':'application/json'},
        body:registerCredentials
        })
        .then(response => response.json())
        .then(data => {
        console.log('received response');
        console.log(data);
        if(data.authorized) {
            // is authorized defined?
        }
        else {
            this.setState({credentialsMatch:false});       
        } 
        
        })
        
    }
    




    render() {
        return (
            <div style={this.getLoginDivStyle()}>
                <h2>Create an account</h2> 
                <br/>
               <Form style={this.getFormStyle()}>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Control type="email" onClick={this.handleEmail} placeholder="Email" required/>
                        <Form.Text className="text-muted"> We'll never share your email with anyone else. </Form.Text>
                    </Form.Group>
                    <Form.Control type='text' placeholder='Enter username' onChange={this.handleUsername} required/>
                    <Form.Group controlId="formBasicPassword">
                        <Form.Control type="password" onClick={this.handlePassword} placeholder="Password" required/>
                        <Form.Control type='password' placeholder='Re-enter password' onChange={this.handleRePassword} required/>
                    </Form.Group>
                    <br/>
                    <h5>I am a: </h5>
                    <ButtonGroup toggle className="mt-2">
                        <ToggleButton type="radio" name="radio" defaultChecked value="1" onClick={this.handleRole}>Candidate</ToggleButton>
                        <ToggleButton type="radio" name="radio" value="2" onClick={this.handleRole}>Recruiter</ToggleButton>
                    </ButtonGroup>
                    
                    <br/>
                    <br/>
                    <Button variant="primary"  onClick={this.handleSubmit} type="submit">Submit</Button>
                </Form>
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

export default Register
