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

  // const posts_items = posts.map((e) => <p className="Button">{e}</p>);
  return (
    <div clasName="PostContainer">
      {posts.map(({ post_text, title, user }) => (
        <div className="Post">
          <p className="post_text">{title}</p>
          <p className="name">{post_text}</p>
          {/* <p className="name">Posted by user {user.user_id}</p> */}
        </div>
      ))}
    </div>
  );
}

export default Post;
