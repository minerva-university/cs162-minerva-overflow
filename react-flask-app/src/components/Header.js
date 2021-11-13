import logo from '../logo.svg';
import React from "react"
import ReactDom from "react-dom"

function Header(props){
    return(
        <div>
            <title>Minerva Overflow</title>
            <a href= "www.minervaoverflow.com">
            <img src={logo} className="App-logo" alt="logo" />
            <h1>Welcome, {props.contact.username}</h1>
            </a>
        </div>
    )
}

export default Header