import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import "./style/NavBar.css";
import { useAuth, logout } from "../auth";

const StyledLink = styled(Link)`
  padding: 20px;
  color: white;
  text-decoration: none;
  &:hover {
    color: pink;
    background: blue;
`;

function NavBar(props) {
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
        <Link to="/home"> Home </Link>{" "}
      </h3>
      {!logged ? (
        <h3 id="login-nav">
          {" "}
          <Link to="/login"> Login </Link>{" "}
        </h3>
      ) : (
        <h3 id="logout-btn" onClick={() => logout()}>
          Logout
        </h3>
      )}
    </div>
  );
}

export default NavBar;

/*
function NavBar(props) {
  return (
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
      {!logged ? (
        <h3 id="login-nav">
          {" "}
          <Link to="/login"> Login </Link>{" "}
        </h3>
      ) : (
        <h3 id="logout-btn" onClick={() => logout()}>
          Logout
        </h3>
      )}
    </div>
  );
}

export default styled(NavBar);
*/
