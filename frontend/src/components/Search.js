import React, { useState } from 'react';
import axios from "axios";
import "./style/Search.css";
import Post from "./Post.js";


export default function Search() {
  const [post_text, setPost] = React.useState("");

  function handleSubmit(e) {
    const user_id = 1;
    const data = { post: { post_text } };

    axios
      .get("/api/search", data)
      .then(() => {
        console.log("searching...");
      })
      .catch((err) => console.log(err));
  }

  return (
    <main>
      <form className="form" onSubmit={handleSubmit}>
        <div className="search_post">
          <input
            className="typingArea"
            type="text"
            placeholder="Search"
            value={post_text}
            onChange={(e) => setPost(e.target.value)}
            required
          />
          <button className="post_button" type="submit">
            Search
          </button>
        </div>
      </form>
      <div className="SearchContent">
        <Post />
      </div>
    </main>
  );
}


/*
class Search extends Component {
  state = {
    posts: null,
    loading: false,
    value: ''
  };

  search = async val => {
    this.setState({ loading: true });
    const res = await axios("/api/search", value);
    const posts = await res.data.results;

    this.setState({ posts, loading: false });
  };

  onChangeHandler = async e => {
    this.search(e.target.value);
    this.setState({ value: e.target.value });
  };

  get renderPosts() {
    let posts = <h1>No posts matching your search</h1>;
    if (this.state.posts) {
      posts = <posts list={this.state.posts} />;
    }

    return posts;
  }

  render() {
    return (
      <div>
        <input
          value={this.state.value}
          onChange={e => this.onChangeHandler(e)}
          placeholder="Type something to search"
        />
        {this.renderPosts}
      </div>
    );
  }
}

export default Search;
*/