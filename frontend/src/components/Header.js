import logo from "../logo.svg";
import React from "react";
import ReactDom from "react-dom";

function Header(props) {
  return (
    <div>
      <title>Minerva Overflow</title>
      <p>Welcome, {props.contact.username}</p>
    </div>
  );
}

export default Header;
