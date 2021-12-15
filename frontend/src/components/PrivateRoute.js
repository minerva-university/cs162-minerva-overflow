import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import {useAuth} from "../auth"

function PrivateRoute({ children }) {
    const [logged] = [useAuth()];
    console.log(logged)
    return logged[0] === false ? <Navigate to='/login'/> : children ;
  }

  export default PrivateRoute
