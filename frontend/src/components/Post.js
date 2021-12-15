import React from "react";
import "./style/Post.css"


function Post(props) {
  var mock_data = {
    name: "Yueh Han Huang",
    user_id: 1,
    city_id: 2,
    post_text: "Bob's Donuts are so so great. I love them!",
  };
  return (
    <div className="Post">
      {/* <Card> */}
      <p className="post_text">{mock_data.post_text}</p>
      <p className="name">Posted by {mock_data.name}</p>
      {/* </Card> */}
    </div>
  );
}

export default Post;
