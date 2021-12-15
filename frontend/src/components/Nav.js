import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import "./style/Nav.css";

const StyledLink = styled(Link)`
  padding: 20px;
  color: white;
  text-decoration: none;
  &:hover {
    color: pink;
    background: blue;
`;

function NavBar(props) {
  return (
    <div class="navbar-top">
      <h3 id="title-nav"> Minerva Overflow / CS162 </h3>
      <h3 id="dashboard-nav">
        {" "}
        <StyledLink to="/">Dashboard</StyledLink>{" "}
      </h3>
      <h3 id="home-nav">
        {" "}
        <StyledLink to="/home"> Home </StyledLink>{" "}
      </h3>
      <h3 id="login-nav">
        {" "}
        <StyledLink to="/login"> Login </StyledLink>{" "}
      </h3>
    </div>
  );
}

export default styled(NavBar);
