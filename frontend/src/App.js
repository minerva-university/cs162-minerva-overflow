import "./App.css";
import React, { useState, useEffect } from "react";
import Header from "./components/Header.js";
import Post from "./components/Post.js";
import NavBar from "./components/Nav.js";
import Elem from "./components/RenderElem.js";
import Tags from "./components/Tags.js";
import MyForm from "./components/MyForm.js";

import Login from './components/Login/Login';
import Dashboard from './components/Dashboard/Dashboard';
import Preferences from './components/Preferences/Preferences';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  const [token, setToken] = useState();

  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className="wrapper">
      <h1>Application</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />}>
          </Route>
          <Route path="/preferences" element={<Preferences />}>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
/*
    <div className="App">
      <NavBar />
      <header className="App-header">
      <MyForm />
        <Header contact={{ username: "XYZ" }} />
        <Post name={"First Post"}></Post>
        <Tags />
        <Elem path="/cohorts" tagName="cohort_name"></Elem>
        <Elem path="/tags" tagName="tag_name"></Elem>
      </header>
    </div>
*/
  );
}

export default App;
