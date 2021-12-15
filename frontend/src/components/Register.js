import React, { useEffect, useState } from "react";
import {login, useAuth, logout} from "../auth"
import {
  Link
} from "react-router-dom";

function Register() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [first_name, setFirstname] = useState('')
    const [surname, setSurname] = useState('')
    const [cohort_id, setCohort] = useState('')
    const [about_me, setAbout] = useState('')

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
        'about_me': about_me
      }}
      fetch('/api/users', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(opts)
      }).then(response => response.json())
      .then(responseJson => {
          console.log(responseJson)
      }, [])
    }

    const checkUsers = (e)=>{
        e.preventDefault()
        fetch('/api/users', {
          method: 'get'
        }).then(response => response.json())
          .then(responseJson => {
              console.log(responseJson)
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

        const handleAboutChange = (e) => {
            setAbout(e.target.value)
        }

    const [logged] = useAuth();
    return (
      <div className='Register'>
        <h2>Registration form</h2>
        {!logged? <form action="#">
          <div>
            <input type="text" 
              placeholder="Username" 
              onChange={handleUsernameChange}
              value={username} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="Password" 
              onChange={handlePasswordChange}
              value={password} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="Email" 
              onChange={handleEmailChange}
              value={email} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="First Name" 
              onChange={handleFirstnameChange}
              value={first_name} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="Surname" 
              onChange={handleSurnameChange}
              value={surname} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="Cohort ID" 
              onChange={handleCohortChange}
              value={cohort_id} 
            />
          </div>
          <div>
            <input type="text" 
              placeholder="My hobbies are..." 
              onChange={handleAboutChange}
              value={about_me} 
            />
          </div>
          <button onClick={onSubmitClick} type="submit">
            Register
          </button>
          <button onClick={checkUsers} type="submit">
            Check
          </button>
        </form>
        : <button onClick={() => logout()}>Logout</button>}
      </div>
    )
  }

export default Register