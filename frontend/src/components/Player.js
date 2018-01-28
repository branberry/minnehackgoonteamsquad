import React, { Component } from 'react';

import '../styles/Player.css';

export default class Player extends Component {

    render() {
        return(
            <div>
                <h3>Player: {this.props.playerName}</h3>
                <h3>Current Injury: {this.props.curInjury}</h3>
                <h3> Injury History: </h3>
            </div>
        );
    }
}