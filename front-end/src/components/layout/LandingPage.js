import React from 'react'
import {Carousel} from 'react-bootstrap';

function LandingPage() {
    return (
        <div>
            <br/>
            <br/>
            <Carousel>
                <Carousel.Item>
                    <img
                    className="d-block w-100"
                    src= {require('../../images/avatar.jpg')}
                    alt="First slide"
                    />
                    <Carousel.Caption>
                    <h3>First slide label</h3>
                    <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                    className="d-block w-100"
                    src= {require('../../images/bread.jpg')}
                    alt="Third slide"
                    />
                    <Carousel.Caption>
                    <h3>Second slide label</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    </Carousel.Caption>
                </Carousel.Item>
            </Carousel>    
        </div>
    )
}

export default LandingPage
