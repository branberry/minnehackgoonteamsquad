import React, { Component } from 'react';
import SidebarContent from './components/Sidebar/SidebarContent';
import MaterialTitlePanel from './components/Sidebar/MaterialTitlePanel';
import Player from './components/Player.js';
import Sidebar from 'react-sidebar';
import {csrftoken }from './components/csrftoken';
//import { Button } from 'reactstrap';
import { HamburgerButton } from 'react-hamburger-button';
import './App.css';

const url = 'http://127.0.0.1:8000/conkdata/';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      docked: false,
      open: false,
      transitions: true,
      touch: true,
      shadow: true,
      pullRight: false,
      touchHandleWidth: 20,
      dragToggleDistance: 30,
      player: {}
    };

    this.renderPropCheckbox = this.renderPropCheckbox.bind(this);
    this.renderPropNumber = this.renderPropNumber.bind(this);
    this.onSetOpen = this.onSetOpen.bind(this);
    this.menuButtonClick = this.menuButtonClick.bind(this);
    this.toggleOpen = this.toggleOpen.bind(this);
  }

  componentDidMount() {
    fetch(url+'getInjuries/')
    .then(response => response.json())
    .then(d => {
      console.log(d);
    });

  // fetch(url+'createUser/', {
  // method: 'POST',
  // headers: {
  //   'Accept': 'application/json',
  //   'Content-Type': 'application/json',
  //   'X-CSRFToken': csrftoken
  // },
  // body: JSON.stringify({
  //   name: 'Carlson Hang',
  //   age: 15,
  //   weight: 150,
  //   height: 67,
  // })
// });

  fetch(url+'createInjury/', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
  body: JSON.stringify({
    user_id : 2,
    injury_type : "concussion",
    symptoms :  "Amnesia,Concentration difficulty,Confusion/disorientation,Dizziness/unsteadiness,Drowsiness",
    bench_date : "",
    unbench_date : ""
  })
});

fetch(url+'unBench/', {
method: 'POST',
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': csrftoken
},
body: JSON.stringify({
  user_id : 1,
  injury_type : "concussion",
  symptoms :  "Amnesia,Concentration difficulty,Confusion/disorientation,Dizziness/unsteadiness,Drowsiness",
  bench_date : "",
  unbench_date : ""
})
});
}

  onSetOpen(open) {
    this.setState({open: open});
  }

  toggleOpen(ev) {
    this.setState({open: !this.state.open});

    if (ev) {
      ev.preventDefault();
    }
  }

  menuButtonClick(ev) {
    ev.preventDefault();
    this.onSetOpen(!this.state.open);
  }

  renderPropCheckbox(prop) {
    const toggleMethod = (ev) => {
      const newState = {};
      newState[prop] = ev.target.checked;
      this.setState(newState);
    };

    return (
      <p key={prop}>
        <input type="checkbox" onChange={toggleMethod} checked={this.state[prop]} id="prop"/>
        <label htmlFor={prop}> {prop}</label>
      </p>
    );
  }

  renderPropNumber(prop) {
    const setMethod = (ev) => {
      const newState = {};
      newState[prop] = parseInt(ev.target.value,10);
      this.setState(newState);
    };

    return (
      <p key={prop}>
        {prop} <input type="number" onChange={setMethod} value={this.state[prop]}/>
      </p>
    );
  }
  render() {
    const sidebar = <SidebarContent/>;

    const sidebarProps = {
      sidebar: sidebar,
      docked: this.state.docked,
      sidebarClassName: 'custom-sidebar-class',
      open: this.state.open,
      touch: this.state.touch,
      shadow: this.state.shadow,
      pullRight: this.state.pullRight,
      touchHandleWidth: this.state.touchHandleWidth,
      dragToggleDistance: this.state.dragToggleDistance,
      transitions: this.state.transitions,
      onSetOpen: this.onSetOpen,
    };

    return(

      <div className="App">
      <Sidebar {...sidebarProps}>

      <MaterialTitlePanel>

      </MaterialTitlePanel>




      </Sidebar>

        <header className="App-header">
        <HamburgerButton className="App-menuButton"
         open={this.state.open} onClick={this.toggleOpen}
         width={40}
          height={40}
          strokeWidth={1}
          rotate={0}
          color='white'
          borderRadius={0}
           animationDuration={0.5}>Menu</HamburgerButton>

          <h1 className="App-title">Injury Monitor</h1>
        </header>


        <h1> Player Profile</h1>
        <Player playerName='Adrian Peterson' curInjury='Mild Concussion'/>

      </div>





    );
  }
}
export default App;


/*
      <div className="App">
        <header className="App-header">

          <h1 className="App-title">Welcome to React</h1>
        </header>
        <h1> Player Profile</h1>
        <Player/>
      </div>




      <div className="App">
          <header className="App-header">
            <h1 className="App-title">Blockchain Addict</h1>
          </header>
          <div className="line-separator"></div>
          <Sidebar {...sidebarProps}>
          <MaterialTitlePanel>
            <button onClick={this.toggleOpen}>Menu</button>
          </MaterialTitlePanel>
        </Sidebar>

      </div>

*/
