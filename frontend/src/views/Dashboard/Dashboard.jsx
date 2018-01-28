import React, { Component } from 'react';
import ChartistGraph from 'react-chartist';
import { Grid, Row, Col } from 'react-bootstrap';

import {
    FormGroup, ControlLabel, FormControl
} from 'react-bootstrap';

import {Card} from 'components/Card/Card.jsx';
import {FormInputs} from 'components/FormInputs/FormInputs.jsx';
import {UserCard} from 'components/UserCard/UserCard.jsx';
import Button from 'elements/CustomButton/CustomButton.jsx';
import {StatsCard} from 'components/StatsCard/StatsCard.jsx';
import {Tasks} from 'components/Tasks/Tasks.jsx';
import {
    dataPie,
    legendPie,
    dataSales,
    optionsSales,
    responsiveSales,
    legendSales,
    dataBar,
    optionsBar,
    responsiveBar,
    legendBar
} from 'variables/Variables.jsx';

class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            
        }
    }
    
    getUser() {

    }


    render() {
        return (
            <div className="content">
                <Grid fluid>
                <form>
                        
                                        <FormInputs
                                            ncols = {["col-md-6"]}
                                            proprieties = {[
                                                {
                                                 label : "Player Name",
                                                 type : "text",
                                                 bsClass : "form-control",
                                                },
                                            ]}
                                        />
                    
                                        <FormInputs
                                            ncols = {["col-md-4","col-md-4","col-md-4"]}
                                            proprieties = {[
                                                {
                                                    label : "Age",
                                                    type : "number",
                                                    bsClass : "form-control",
                                                    placeholder : "City",
                                                },
                                                {
                                                    label : "Weight (lbs)",
                                                    type : "number",
                                                    bsClass : "form-control",
                                                    placeholder : "Country",
                                                },
                                                {
                                                    label : "Height (in)",
                                                    type : "number",
                                                    bsClass : "form-control",

                                                }
                                            ]}
                                        />

                              
                                        <Button
                                            bsStyle="info"
                                            pullRight
                                            fill
                                            type="submit"
                                            
                                        >
                                        
                                        </Button>
                                        <div className="clearfix"></div>
                                    </form>
                </Grid>
            </div>
        );
    }
}

export default Dashboard;
