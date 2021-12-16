import React, { useState, useEffect } from "react";
import "./style/Dashboard.css";
import Header from "./Header.js";
import Post from "./Post.js";
import Elem from "./RenderElem.js";
import Tags from "./Tags.js";
import Addposts from "./Addposts.js";
import Login from "./Login";
import { useAuth } from "../auth";
import { getAutomaticTypeDirectiveNames } from "typescript";

function Dashboard() {
  const [logged] = [useAuth()];

  if (!logged[0]) {
    return <Login />;
  }
  return (
    <div className="Dashboard">
      <div className="App-header">
        <div className="AppMenu">
          <Addposts />
          <Elem path="/api/cohorts" tagName="cohort_name"></Elem>
          <Elem path="/api/tags" tagName="tag_name"></Elem>
        </div>
        <div className="AppContent">
          <Post />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
