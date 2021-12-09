import React from "react";
import "./Post.css";
import UPVOTE from "./images/upvote.png";
import DOWNVOTE from "./images/downvote.png";

function Post(props) {
  var mock_data = {
    name: "Yueh Han Huang",
    user_id: 1,
    city_id: 2,
    upvote: 31,
    date: "2021/10/07",
    title: "Best Donuts in USA",
    post_text: "Bob's Donuts are so so great. I love them!",
  };
  return (
    <div className="Post">
      {/* <Card> */}
      <div className="votes">
      <button onClick="uparrow">
      <img src={UPVOTE} alt="button" />
      </button>
      <p>{mock_data.upvote}</p>
      <button onClick="downvote">
      <img src={DOWNVOTE} alt="button" />
      </button>
      </div>
      
      <div className="post_info">
        <h4>{mock_data.title}</h4>
        <p>{mock_data.post_date}</p>
        <p>{mock_data.post_text}</p>
        <p>Posted by {mock_data.name}</p>
      </div>
      {/* </Card> */}
    </div>
  );
}

export default Post;
