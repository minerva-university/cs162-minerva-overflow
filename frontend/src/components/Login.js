import React, { useEffect, useState } from "react";
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
        <form action="#">
          <div>
            <input
              type="text"
              placeholder="Username"
              onChange={handleUsernameChange}
              value={username}
            />
          </div>
          <div>
            <input
              type="password"
              placeholder="Password"
              onChange={handlePasswordChange}
              value={password}
            />
          </div>
          <button onClick={onSubmitClick} type="submit">
            Login Now
          </button>
          <div>
            <h3> Don't have an account? Create one!</h3>
            <Link to ='/register'> <button> Register </button> </Link>
          </div>
        </form>
      ) : (
        <button onClick={() => logout()}>Logout</button>
      )}
    </div>
  );
}

export default Login;
