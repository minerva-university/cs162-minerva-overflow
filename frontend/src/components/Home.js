import React, { useState, useEffect } from "react";
import "./style/Home.css";

function Home() {
  /*
    if(!token) {
      return <Login setToken={setToken} />
    }
    */
    var mock_data = {
      name: "Allison Lehn",
      user_id: 2,
      email : "allison@uni.minerva.edu"
    };
  return (
    <div className="Home">
      <header className="App-head">
        <h2> Welcome to your home, {mock_data.name}!</h2>
      </header>
      <p>email : {mock_data.email}</p>
      <h3>My Posts</h3>
      {/* get_posts_written_by_user here */}
      <h3>My Comments</h3>
      {/* get_comments_written_by_user here */}
    </div>
  );
}

export default Home;
