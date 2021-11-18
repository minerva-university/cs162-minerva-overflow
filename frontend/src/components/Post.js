import React from "react";

function Post(props) {
  var mock_data = {
    name: "Yueh Han Huang",
    user_id: 1,
    city_id: 2,
    title: "Best Donuts in USA",
    post_text: "Bob's Donuts are so so great. I love them!",
  };
  return (
    <div className="Button">
      {/* <Card> */}
      <h4>{mock_data.title}</h4>
      <p>{mock_data.post_text}</p>
      <p>Posted by {mock_data.name}</p>
      {/* </Card> */}
    </div>
  );
}

export default Post;
