import React, { useEffect, useState } from "react";
import {login, useAuth, logout} from "../auth"
import {
  Link, 
  useNavigate
} from "react-router-dom";
import "./style/Register.css";
import Login from './Login';

function Register() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [first_name, setFirstname] = useState('')
    const [surname, setSurname] = useState('')
    const [cohort_id, setCohort] = useState('')
    let history = useNavigate();

    const onSubmitClick = (e)=>{
      e.preventDefault()
      let opts = {
      'user':{
        'username': username,
        'password': password,
        'email': email,
        'first_name': first_name,
        'surname': surname,
        'cohort_id': cohort_id,
        'about_me': ' ',
      }}
      fetch('/api/users', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(opts)
      }).then(response => response.json())
      .then(responseJson => {if (responseJson.status==='SUCCESS') {
            history("/login")
        }
      })
    }

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    const handleFirstnameChange = (e) => {
        setFirstname(e.target.value)
    }

    const handleSurnameChange = (e) => {
        setSurname(e.target.value)
    }

    const handleEmailChange = (e) => {
        setEmail(e.target.value)
    }

    const handleCohortChange = (e) => {
        setCohort(e.target.value)
    }

    const [logged] = useAuth();
    return (
      <div className='Register'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          </link>
        <h2>Registration form</h2>
        {!logged? <form id="sign-up-form"  action="#">
          <div className="form-group">
            <input type="text" 
              placeholder="Username" 
              onChange={handleUsernameChange}
              value={username}
              className="form-control" 
            />
          </div>
          <div className="form-group">
            <input type="password" 
              placeholder="Password" 
              onChange={handlePasswordChange}
              value={password} 
              className="form-control"
            />
          </div>
          <div className="form-group">
            <input type="text" 
              placeholder="Email" 
              onChange={handleEmailChange}
              value={email} 
              className="form-control"
            />
          </div>
          <div className="form-group">
            <input type="text" 
              placeholder="First Name" 
              onChange={handleFirstnameChange}
              value={first_name} 
              className="form-control"
            />
          </div>
          <div className="form-group">
            <input type="text" 
              placeholder="Surname" 
              onChange={handleSurnameChange}
              value={surname} 
              className="form-control"
            />
          </div>
          <div className="form-group">
            <input type="text" 
              placeholder="Cohort ID" 
              onChange={handleCohortChange}
              value={cohort_id} 
              className="form-control"
            />
          </div>
          <br/>
          <button id='register-btn' className="btn btn-primary btn-block" onClick={onSubmitClick} type="submit">
            Register
          </button>
        </form>
        : <button onClick={() => logout()}>Logout</button>}
      </div>
    )
  }

export default Register