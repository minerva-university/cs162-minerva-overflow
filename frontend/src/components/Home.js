import React, { useState, useEffect } from "react";
import { useAuth } from "../auth";
import Login from './Login';
function Home() {
    
    const [logged] = [useAuth()];
    
    
    if(!logged[0]) {
      setTimeout(() => {  return <Login/>; }, 500);
    }
  
    return (
      <div className="Home">
        <p> This is your home!</p>
      </div>
    );
  }
  
  export default Home;