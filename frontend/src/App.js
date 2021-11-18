import "./App.css";
import React, { useState, useEffect } from "react";
import Header from "./components/Header.js";
import Post from "./components/Post.js";
// import Tags from "./components/Tags.js";

function App() {
  const [tagSize, setTagSize] = useState(1);
  useEffect(() => {
    fetch("/tags")
      .then((res) => res.json())
      .then((data) => {
        setTagSize(JSON.stringify(data.map((obj) => obj.tag_name)));
      });
  }, []);

  const [cohorts, setCohorts] = useState(1);
  useEffect(() => {
    fetch("/cohorts")
      .then((res) => res.json())
      .then((data) => {
        setCohorts(JSON.stringify(data.map((obj) => obj.cohort_name)));
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <Header contact={{ username: "XYZ" }} />
        <Post name={"First Post"}></Post>
        <Post name={"Second Post"}></Post>
        <Post name={"Third Post"}></Post>
        {/* <Tags></Tags> */}
        <p>{tagSize}</p>
        <p>{cohorts}</p>
      </header>
    </div>
  );
}

export default App;
