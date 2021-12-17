import axios from "axios";
import React, { useState, useEffect } from "react";
import "./style/Post.css";

function Post() {
  //A post component that is filled in when called in AddPost
  const [posts, setPosts] = useState([{}]);
  const [loading, setIsLoading] = useState(true);
  useEffect(() => {
    axios
      .get("/api/posts")
      .then((res) => {
        console.log(res.data);
        setPosts(res.data);
        setIsLoading(false);
      })
      .catch((err) => console.log(err));
  }, []);

  if (loading) {
    return <div> Loading ... </div>;
  }

  return (
    <div clasName="PostContainer">
      {posts.map((post) => {
        return (
          <div className="Post">
            <h3 className="post_title">{post.title}</h3>

            <p className="post_author">
              Posted by {post.user.first_name} {post.user.surname}
            </p>
            <p className="post_author">In {post.city.city_name}</p>
            {post.tags.map((tag) => (
              <button className="Button">#{tag.tag_name}</button>
            ))}
            <p className="post_text">{post.post_text}</p>
          </div>
        );
      })}
    </div>
  );
}

export default Post;
