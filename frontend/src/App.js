import "./App.css";
import React from "react";
import NavBar from "./components/Nav.js";
import Tags from "./components/Tags.js";

function App() {
  return (
    <div className="App">
      <NavBar />
      <div className="App-header">
        <Tags />
      </div>
    </div>
  );
}

export default App;
