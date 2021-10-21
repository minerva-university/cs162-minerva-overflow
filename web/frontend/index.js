import React from "react";
import ReactDOM from "react-dom";
// import Draggable from "react-draggable";
// import "tailwindcss/tailwind.css";

const destination = document.getElementById("root");

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      color: "#ddd",
    };
  }
  render() {
    document.body.style.backgroundColor = this.state.color;
    return <div>Current background color {this.state.color}</div>;
  }
}

ReactDOM.render(<App />, destination);
