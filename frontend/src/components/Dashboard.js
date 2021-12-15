import React, { useState, useEffect } from "react";
import Header from "./Header.js";
import Post from "./Post.js";
import Elem from "./RenderElem.js";
import Tags from "./Tags.js";
import {useAuth} from "../auth"
import Login from './Login';

function Dashboard() {
  
    const [logged] = [useAuth()];

    if(!logged[0]) {
      return <Login/>
    }

    return (
      <div className="Dashboard">
        <header className="App-header">
          <Header contact={{ username: "XYZ" }} />
          <Post name={"First Post"}></Post>
          <Tags />
          <Elem path="/cohorts" tagName="cohort_name"></Elem>
          <Elem path="/tags" tagName="tag_name"></Elem>
        </header>
      </div>
    );
  }
  
  export default Dashboard;