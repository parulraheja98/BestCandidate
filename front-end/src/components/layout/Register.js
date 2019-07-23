import React, { Component } from 'react'
import {Form, Button, Alert, ButtonGroup, ToggleButton} from 'react-bootstrap'


export class Register extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username :'',
            password :'',
            firstname : '',
            lastname : '',
            title : '', // only for recruiter
            company : '',//
            confPassword :'',
            credentialsMatch :true,
            role : '',
            successsfulRegistration : false,
            minLength : 3,
            showRecruiterFields : false,
            allFieldsComplete : true
        };
    }

    
    handleChange = event => {
        console.log(event.target.id+" updating to "+event.target.value);
        this.setState({
          [event.target.id]: event.target.value
        });
    }
    
    handleRole(event) {
        console.log('role changed to ', event.target.value);
        this.setState({role: event.target.value});
    }

    verifyState = () => {
        if(this.state.role == "candidate"){
            if(typeof this.state.username !== 'undefined' && typeof this.state.firstname !== 'undefined'
                    && typeof this.state.lastname !== 'undefined'){
                        console.log("all fields for candidate filled");
                        return true;
            }
        }else if(this.state.role === "recruiter"){
            if(typeof this.state.username !== 'undefined' && typeof this.state.firstname !== 'undefined'
                    && typeof this.state.lastname !== 'undefined' && typeof this.state.title !== 'undefined'
                    && typeof this.state.company !== 'undefined'){
                        console.log("all fields for recruiter filled");
                        return true;
            }
        }
        return false;
    }

    

    handleSubmit(event) {

        event.preventDefault();
        console.log("sending "+this.state.username+" and "+this.state.password+" as "+this.state.role);

        if(this.verifyState()){
            if(this.state.password === this.state.confPassword){
    
                console.log("Passwords match");
                
                var candidateRoute = 'http://localhost:5000/candidates'
                var recruiterRoute = 'http://localhost:5000/recruiters'
                var route;

                var registrationData;

                if( this.state.role === "candidate"){
                    console.log("packing post as candidate");
                    registrationData = JSON.stringify({
                        username : this.state.username,
                        password : this.state.password,
                        firstname : this.state.firstname,
                        lastname : this.state.lastname,
                        role: this.state.role
                    })
                    route = candidateRoute;
                }else if( this.state.role === "recruiter"){
                    console.log("packing post as recruiter");
                    registrationData = JSON.stringify({
                        username : this.state.username,
                        password : this.state.password,
                        firstname : this.state.firstname,
                        lastname : this.state.lastname,
                        title : this.state.title,
                        company : this.state.company
                    })
                    route = recruiterRoute;
                }

                //only proceed if the route has been assigned
                if(typeof route !== 'undefined' && typeof registrationData !== 'undefined'){
                    console.log("Route has been assigned ", route, registrationData);
                    fetch(route , {
                    method:'POST',
                    credentials:'include',
                    headers:{'Content-Type':'application/json'},
                    body: registrationData
                    })
                    .then(response => response.json())
                    .then(response => {
                    console.log('Received response');
                    console.log(response);
                    if(response.ok) {
                        console.log("Successful registration"); //display succesful registration alert
                        this.setState({successsfulRegistration: true});
                    
                        //redirect to the appropiate login page
                        if(this.state.role === "recruiter"){
                            this.props.history.push('/recruiter-login'); //redirect to candidat page
                        }else if(this.state.role === "candidate"){
                            this.props.history.push('/candidate-login'); //redirect to candidat page
                        }
                    }
                    
                    })
                }else{
                    console.log("role or registration payload are undefined");
                }    
            }else{
                console.log(this.state.password+" match "+this.state.confPassword);
                this.setState({credentialsMatch:false, successsfulRegistration:false}); //display credentials match alert
                console.log("Passwords do not match");
            }    
        }else{
            console.log("All fields are not complete");
            this.setState({allFieldsComplete: false});
        }
    }
    




    render() {
        return (
            <div style={this.getLoginDivStyle()}>
                <h2>Create an account</h2> 
                <br/>
               <Form style={this.getFormStyle()}> 
                    {this.state.credentialsMatch ? null :<Alert variant='danger'>{this.state.role} credentials do not match.</Alert>}
                    {this.state.allFieldsComplete ? null :<Alert variant='warning'>Please enter all fields..</Alert>}
                    {this.state.successsfulRegistration ?<Alert variant='success'>{this.state.role} account created.</Alert>:null}                   
                    <Form.Group controlId="firstname">    
                        <Form.Control autoFocus type='text'  value={this.state.firstname} placeholder='first name' onChange={this.handleChange} required/>
                    </Form.Group>
                    <Form.Group controlId="lastname">    
                        <Form.Control  type='text'  value={this.state.lastname} placeholder='last name' onChange={this.handleChange} required/>
                    </Form.Group>
                    <Form.Group controlId="username">    
                        <Form.Control autoFocus type='text'  value={this.state.username} placeholder='username' onChange={this.handleChange} required/>
                        <Form.Text className="text"> username must be at least {this.state.minLength} characters long.</Form.Text>
                    </Form.Group>

                    <br/>
                    <h5>I am a: </h5>
                    <ButtonGroup toggle className="mt-2" style={this.getCheckboxStyle()}>
                        <br/>
                        <ToggleButton defaultChecked type="radio" name="radio"  value="candidate" onChange={this.handleRole.bind(this)}>Candidate</ToggleButton>
                        <ToggleButton  type="radio" name="radio" value="recruiter" onChange={this.handleRole.bind(this)}>Recruiter</ToggleButton>
                    </ButtonGroup>
                    <br/>

                    {this.state.role === "recruiter" ? 
                    <div>
                        <Form.Group controlId="title">    
                            <Form.Control autoFocus type='text'  value={this.state.title} placeholder='Job title' onChange={this.handleChange} required/>
                        </Form.Group> 
                        <Form.Group controlId="company">    
                            <Form.Control type='text'  value={this.state.company} placeholder='Company name' onChange={this.handleChange} required/>
                        </Form.Group>
                    </div>    
                    : null                    
                    }
                     <br/>
                    <Form.Group controlId="password">
                        <Form.Control type="password" value={this.state.password} onChange={this.handleChange} placeholder="Password" required/>
                    </Form.Group>


                    <Form.Group controlId="confPassword">
                        <Form.Control type='password' value={this.confPassword}  onChange={this.handleChange} placeholder='Re-enter password' required/>
                    </Form.Group>
                    
                    
                    <Button block  variant="primary" onClick={this.handleSubmit.bind(this)} type="submit">Register {this.state.role}</Button>
                </Form>
            </div>
            
        )
    }

    

    getCheckboxStyle = () => {
        return {
            marginTop : '20px',
            marginBottom : '20px'
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

export default Register
