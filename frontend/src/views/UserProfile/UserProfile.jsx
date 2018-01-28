import React, { Component } from 'react';
import {
    Grid, Row, Col,
    FormGroup, ControlLabel, FormControl
} from 'react-bootstrap';

import {Card} from 'components/Card/Card.jsx';
import {FormInputs} from 'components/FormInputs/FormInputs.jsx';
import {UserCard} from 'components/UserCard/UserCard.jsx';
import Button from 'elements/CustomButton/CustomButton.jsx';

import avatar from "assets/img/faces/face-3.jpg";

class UserProfile extends Component {
    constructor(props) {
        super(props);

        this.state = {
            name: '',
            age: 0,
            weight: 0,
            u_id: 2,
            bench_date: '',
            unbench_date: '',
            injuryHistory: {},
            createInjury: {}
        }
        this.getInjuries.bind(this);
        this.getUser.bind(this);
        this.createInjury.bind(this);
    }

    getInjuries(id) {
        fetch('http://127.0.0.1:8000/conkdata/getInjury/'+id)
        .then(results => results.json())
        .then(d => {
            let injuries = Object.assign({}, this.injuryHistory);
            injuries = d;
            console.log(d);
            this.setState({injuryHistory:injuries});
        });
    }

    getUser() {
        fetch('http://127.0.0.1:8000/conkdata/get/'+this.id)
        .then(results => results.json())
        .then(d => {
            let injuries = Object.assign({}, this.injuryHistory);
            injuries = d;
            console.log(d);
            this.setState({injuryHistory:injuries});
        });
    }

    createInjury(prop) {
        fetch('http://127.0.0.1:8000/conkdata/createInjury/')
        .then(results => {
            console.log(results)
        })
        /*  .then(d => {
            let injuries = Object.assign({}, this.injuryHistory);
            injuries = d;
            console.log(d);
            this.setState({injuryHistory:injuries});
        });*/
    }
    render() {
        
        return (
            <div className="content">
                <Grid fluid>
                    <Row>
                        <Col md={8}>
                            <Card
                                title="Edit Profile"
                                content={
                                    <form onSubmit={this.createInjury(this)}>
                                        <FormInputs
                                            ncols = {["col-md-5" , "col-md-3" ]}
                                            proprieties = {[
                                                {
                                                 label : "Injury Type",
                                                 type : "text",
                                                 bsClascds : "form-control",
                                                },
                                                {
                                                 label : "Symptom",
                                                 type : "text",
                                                 bsClass : "form-control",
                                                }
                                            ]}
                                        />
                                        <FormInputs
                                            ncols = {["col-md-4" , "col-md-4","col-md-4"]}
                                            proprieties = {[
                                                {
                                                 label : "Height (in)",
                                                 type : "text",
                                                 bsClass : "form-control",
                                                 placeholder : "First name",
                                                 defaultValue : "Mike"
                                                },
                                                {
                                                 label : "Weight (lbs)",
                                                 type : "text",
                                                 bsClass : "form-control",
                                                },
                                                {
                                                 label: "Age",
                                                 type: "number"
                                                }
                                            ]}
                                        />
                                        
 
                                        <Button
                                            bsStyle="info"
                                            pullRight
                                            fill
                                            type="submit"
                                        >
                                            Bench
                                        </Button>
                                        <div className="clearfix"></div>
                                    </form>
                                }
                            />
                        </Col>
                        <Col md={4}>
                            <UserCard
                                bgImage="https://ununsplash.imgix.net/photo-1431578500526-4d9613015464?fit=crop&fm=jpg&h=300&q=75&w=400"
                                avatar={avatar}
                                name="Mike Andrew"
                                userName="michael24"
                                socials={
                                    <div>

                                    </div>
                                }
                            />
                        </Col>

                    </Row>
                </Grid>>
            </div>
        );
    }
}

export default UserProfile;
