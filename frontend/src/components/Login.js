import React, { useEffect, useState, Component } from "react";
import { login, useAuth, logout } from "../auth";
import "./style/Login.css";
import {Link } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const onSubmitClick = (e) => {
    e.preventDefault();
    let opts = {
      username: username,
      password: password,
    };
    //console.log(opts)
    fetch("/api/login", {
      method: "post",
      body: JSON.stringify(opts),
    })
      .then((r) => r.json())
      .then((token) => {
        if (token.access_token) {
          login(token);
          //console.log(token)
        } else {
          //console.log("Please type in correct username/password")
        }
      });
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const [logged] = useAuth();

  return (
    <div className="Login">
      <h2>Login</h2>
      {!logged ? (
        <form id="sign-in-form" action="#">
          <div className="form-group">
            <input
              type="text"
              placeholder="Username"
              onChange={handleUsernameChange}
              value={username}
              className="form-control" 
            />
          </div>
          <div className="form-group">
            <input
              type="password"
              placeholder="Password"
              onChange={handlePasswordChange}
              value={password}
              className="form-control" 
            />
          </div >
          <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
          </div>
          <div className="form-group">
          <button className="btn btn-primary btn-block" onClick={onSubmitClick} type="submit">
            Login Now
          </button>
          </div>
          <div className="form-group">
            <h6> Don't have an account? Create one!</h6>
            <Link to ='/register'> <button className="btn btn-primary btn-block" > Register </button> </Link>
          </div>
        </form>
      ) : (
        <button className="btn btn-primary btn-block" onClick={() => logout()}>Logout</button>
      )}
    </div>
  );
}

export default Login;

