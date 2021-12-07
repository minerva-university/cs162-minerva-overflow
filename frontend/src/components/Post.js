import React from "react";

function Post(props) {
  var mock_data = {
    name: "Yueh Han Huang",
    user_id: 1,
    city_id: 2,
    upvote: 31,
    title: "Best Donuts in USA",
    post_text: "Bob's Donuts are so so great. I love them!",
  };
  return (
    <div className="Post">
      {/* <Card> */}
      <div class='uparrow'>
        <button >upvote</button>
        <p>{mock_data.upvote}</p>
      </div>
      <div className='post_info'>
        <h4>{mock_data.title}</h4>
        <p>{mock_data.post_text}</p>
        <p>Posted by {mock_data.name}</p>
      </div>
      {/* </Card> */}
    </div>
  );
}

export default Post;
