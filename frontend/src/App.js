import "./App.css";
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Home from "./components/Home";
import Login from "./components/Login";
//import NavBar from "./components/Nav";

//import {useAuth} from "./auth"
import Register from "./components/Register";
import NavBar from "./components/NavBar";
import { useAuth, authFetch } from "./auth";
// import "../node_modules/bootstrap/dist/css/bootstrap.min.css";

function App() {
  /*
  const [token, setToken] = useState();
  if(!token) {
    return <Login setToken={setToken} />
  }
  */
  const [logged] = useAuth();
  return (
    <Router>

      <div id="app">

        {logged ? <NavBar /> : <div></div>}
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
