import React, { Component } from 'react'
import { Table } from 'react-bootstrap'

export class Candidate extends Component {
    
    
    constructor(props){
        super(props);
        const { cookies } = props;
        this.state = {
            userInfo : []
        };
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    render() {
        return (
            <div>
                <h2>Good afternoon NAME</h2>
                <div>
                    <h3>My applications <i className="material-icons">work</i></h3>
                    https://dev.to/abdulbasit313/an-easy-way-to-create-a-customize-dynamic-table-in-react-js-3igg
                    <Table striped bordered hover>
                        <thead>
                            <tr>
                            <th>Title</th>
                            <th>Description</th>
                            <th>Posted by</th>
                            <th>Status</th>
                            <th>Deadline</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                            </tr>
                            <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                            </tr>
                            <tr>
                            <td>3</td>
                            <td colSpan="2">Larry the Bird</td>
                            <td>@twitter</td>
                            </tr>
                        </tbody>
                    </Table>
                </div>
            </div>
        )
    }
}

export default Candidate
