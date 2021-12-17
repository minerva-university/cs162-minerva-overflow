import React from "react";
import { Link } from "react-router-dom";
import "./style/NavBar.css";
import { useAuth, logout } from "../auth";

function NavBar(props) {
  //Navbar that contains links to different parts of the application
  const [logged] = useAuth();
  return (
    <div class="navbar-top">
      <h3 id="title-nav"> Minerva Overflow / CS162 </h3>
      <h3 id="dashboard-nav">
        {" "}
        <Link to="/">Dashboard</Link>{" "}
      </h3>
      <h3 id="home-nav">
        {" "}
        <Link to="/home">Home</Link>{" "}
      </h3>
      {!logged ? (
        <h3 id="login-nav">
          {" "}
          <Link to="/login"> Login </Link>{" "}
        </h3>
      ) : (
        <h3 id="logout-btn" onClick={() => logout()}>
          <a>Logout</a>
        </h3>
      )}
    </div>
  );
}

export default NavBar;

