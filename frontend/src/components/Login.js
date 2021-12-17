import React, { useEffect, useState, Component } from "react";
import { login, useAuth, logout } from "../auth";
import "./style/Login.css";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function Login() {
  //Login componen that contains a form that validates data in the
  //user database and issues a token for the logged in user
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  let history = useNavigate();

  const onSubmitClick = (e) => {
    e.preventDefault();
    let opts = {
      username: username,
      password: password,
    };
    fetch("/api/login", {
      method: "post",
      body: JSON.stringify(opts),
    })
      .then((r) => r.json())
      .then((token) => {
        if (token.access_token) {
          login(token);
        } else {
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
      <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"
      ></link>
      {!logged ? (
      <div> 
        <h2>Login</h2>
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
          </div>
          <div className="form-group">
            <div className="custom-control custom-checkbox">
              <input
                type="checkbox"
                className="custom-control-input"
                id="customCheck1"
              />
              <label className="custom-control-label" htmlFor="customCheck1">
                Remember me
              </label>
            </div>
          </div>
          <div className="form-group">
            <button
              className="btn btn-primary btn-block"
              onClick={onSubmitClick}
              type="submit"
            >
              Login Now
            </button>
          </div>
          <div className="form-group">
            <h6> Don't have an account? Create one!</h6>
            <Link to="/register">
              {" "}
              <button className="btn btn-primary btn-block">
                {" "}
                Register{" "}
              </button>{" "}
            </Link>
          </div>
        </form>
      </div>
      ) : (
         history("/home")
      )}
    </div>
  );
}

export default Login;
