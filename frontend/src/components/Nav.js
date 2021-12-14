import React from "react";
import {Link} from "react-router-dom";

function NavBar(props) {
  return (
    <div class='navbar-top'>
            <h3 id='title-nav'> Minerva Overflow / CS162 </h3>
            <h3 id='dashboard-nav'> <Link to='/'>Dashboard</Link> </h3>
            <h3 id='home-nav'> <Link to='/home'> Home </Link> </h3>
            <h3 id='login-nav'> <Link to='/login'> Login </Link> </h3>
      </div>
  );
}

export default NavBar;
