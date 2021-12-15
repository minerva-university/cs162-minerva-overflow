import "./App.css";
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Home from "./components/Home";
import Login from "./components/Login";
import NavBar from "./components/Nav";
import Addposts from "./components/Addposts";

function App() {
  /*
  const [token, setToken] = useState();
  if(!token) {
    return <Login setToken={setToken} />
  }
  */

  return (
    <Router>
      <div>
        <div class="navbar-top">
          <h3 id="title-nav"> Minerva Overflow / CS162 </h3>
          <h3 id="dashboard-nav">
            {" "}
            <Link to="/">Dashboard</Link>{" "}
          </h3>
          <h3 id="home-nav">
            {" "}
            <Link to="/home"> Home </Link>{" "}
          </h3>
          <h3 id="login-nav">
            {" "}
            <Link to="/login"> Login </Link>{" "}
          </h3>
        </div>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
