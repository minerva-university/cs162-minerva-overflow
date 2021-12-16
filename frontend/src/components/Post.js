import React, { useState, useEffect } from "react";
import "./style/Post.css";

function Post() {
  const [posts, setPosts] = useState(["loading..."]);
  useEffect(() => {
    fetch("api/posts", { method: "get" })
      .then((response) => {
        if (response.status === 401) {
          setPosts(["Sorry you aren't authorized!"]);
          return null;
        }
        return response.json();
      })
      .then((response) => {
        if (response) {
          setPosts(response);
        }
      });
  }, []);

  var mock_data = {
    name: "Yueh Han Huang",
    user_id: 1,
    city_id: 2,
    post_text: "Bob's Donuts are so so great. I love them!",
  };

  // const posts_items = posts.map((e) => <p className="Button">{e}</p>);
  console.log(posts);
  return (
    <div clasName="PostContainer">
      {posts.map(({ post_text, title, user_id }) => (
        <div className="Post">
          <p className="post_text">{post_text}</p>
          <p className="name">{title}</p>
          <p className="name">Posted by user {user_id}</p>
        </div>
      ))}
    </div>
  );
}

export default Post;
