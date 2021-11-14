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

  return (
    <div className="App">
      <header className="App-header">
        <Header contact={{ username: "XYZ" }} />
        <Post name={"First Post"}></Post>
        <Post name={"Second Post"}></Post>
        {/* <Tags></Tags> */}
        <p>{tagSize}</p>
      </header>
    </div>
  );
}

export default App;
