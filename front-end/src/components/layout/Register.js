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
            role: '',
            successsfulRegistration: false,
            minLength: 3
        };
    }

    validateForm(){
        return (this.state.username.length > this.state.minInputLength &&
            this.state.password.length > this.state.minInputLength);
    }
    
    handleChange = event => {
        //console.log(event.target.id+" updating to "+event.target.value);
        console.log("the ussername is "+this.state.username);
        console.log("the password is "+this.state.password);
        this.setState({
          [event.target.id]: event.target.value
        });
      }
    
      handleRole(event) {
          console.log('event name ', event.target.name);
           console.log('checking event', event.target.checked);
           console.log('checking value', event.target.value);
           this.setState({role: event.target.value});
      }

    handleSubmit(event) {

        event.preventDefault();
        console.log("sending "+this.state.username+" and "+this.state.password);

        if(this.state.password === this.state.confPassword){
   
            console.log("Passwords match");

            var registerCredentials = JSON.stringify({
                username:this.state.username,
                password:this.state.password,
                role: this.state.role
            })

            fetch('http://localhost:5000/register' , {
            method:'POST',
            credentials:'include',
            headers:{'Content-Type':'application/json'},
            body:registerCredentials
            })
            .then(response => response.json())
            .then(response => {
            console.log('received response');
            console.log(response);
            if(response.message) {
                console.log("Successful registration"); //display succesful registration alert
                this.setState({successsfulRegistration: true});
                this.props.history.push('/candidate'); //redirect to candidat page
            }
            
            })
        }else{
            console.log(this.state.password+" match "+this.state.confPassword);
            this.setState({credentialsMatch:false, successsfulRegistration:false}); //display credentials match alert
            console.log("Passwords do not match");

        }    
        
    }
    




    render() {
        return (
            <div style={this.getLoginDivStyle()}>
                <h2>Create an account</h2> 
                <br/>
               <Form style={this.getFormStyle()}> 
                    {this.state.credentialsMatch ?null :<Alert variant='danger'>{this.state.role} credentials do not match.</Alert>}
                    {this.state.successsfulRegistration ?<Alert variant='success'>{this.state.role} account created.</Alert>:null}
                    <Form.Group controlId="username">    
                        <Form.Control autoFocus type='text'  value={this.state.username} placeholder='Enter username' onChange={this.handleChange} required/>
                        <Form.Text className="text"> username must be at least {this.state.minLength} characters long.</Form.Text>
                    </Form.Group>

                    <Form.Group controlId="password">
                        <Form.Control type="password" value={this.state.password} onChange={this.handleChange} placeholder="Password" required/>
                    </Form.Group>


                    <Form.Group controlId="confPassword">
                        <Form.Control type='password' value={this.confPassword}  onChange={this.handleChange} placeholder='Re-enter password' required/>
                    </Form.Group>
                    
                    
                    <br/>
                    <h5>I am a: </h5>
                    <ButtonGroup toggle className="mt-2">
                        <ToggleButton type="radio" name="radio" defaultChecked value="candidate" onChange={this.handleRole.bind(this)}>Candidate</ToggleButton>
                        <ToggleButton  type="radio" name="radio" value="recruiter" onChange={this.handleRole.bind(this)}>Recruiter</ToggleButton>
                    </ButtonGroup>
                    
                    <br/>
                    <br/>
                    <Button block  variant="primary" onClick={this.handleSubmit.bind(this)} type="submit">Register</Button>
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
