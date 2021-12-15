import React, { useState, useEffect } from "react";
import "./style/Dashboard.css";
import Header from "./Header.js";
import Post from "./Post.js";
import Elem from "./RenderElem.js";
import Tags from "./Tags.js";
import Addposts from "./Addposts";

function Dashboard() {
  /*
    if(!token) {
      return <Login setToken={setToken} />
    }
    */

  return (
    <div className="Dashboard">
      <header className="App-header">
        <Header contact={{ username: "XYZ" }} />
        <Addposts />
        <Post name={"First Post"}></Post>
        <Tags />
        <Elem path="/cohorts" tagName="cohort_name"></Elem>
        <Elem path="/tags" tagName="tag_name"></Elem>
      </header>
    </div>
  );
}

export default Dashboard;
