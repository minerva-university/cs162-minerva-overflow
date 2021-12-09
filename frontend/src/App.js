import "./App.css";
import React, { useState, useEffect } from "react";
import Header from "./components/Header.js";
import Post from "./components/Post.js";
import NavBar from "./components/Nav.js";
import Elem from "./components/RenderElem.js";
// import Tags from "./components/Tags.js";

function App() {
  return (
    <div className="App">
      <NavBar />
      <header className="App-header">
        <Elem path="/cohorts" tagName="cohort_name"></Elem>
        <Elem path="/tags" tagName="tag_name"></Elem>
        <Post name={"First Post"}></Post>
        <Post name={"First Post"}></Post>
        <Post name={"First Post"}></Post>
      </header>
    </div>
  );
}

export default App;
