import React, { Component } from 'react';
import { Button } from 'reactstrap';
import '../styles/Player.css';

export default class Player extends Component {
    constructor(props) {
        super(props); 
        this.state = {
            playerName: 'Adrian Peterson',
            playerId: 0,
            playerHistory: {}
        }
    }

    render() {
        return(
            <div>
                <h2>{this.state.playerName}</h2>

            </div>
        );
    }
}