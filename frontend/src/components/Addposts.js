import React from "react";
import axios from "axios";
import "./style/Addposts.css";

export default function Addposts() {
  //A function used to add a post to the dashboard
  //it collects data from the cities, tags, and protected APIs
  const [city_id, setCity] = React.useState(1);
  const [post_text, setPost] = React.useState("");
  const [title, setTitle] = React.useState("");
  const [tag, setTag] = React.useState(1);

  const [allCities, setAllCities] = React.useState([]);
  const [allTags, setAllTags] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/cities")
      .then((res) => setAllCities(res.data))
      .catch((err) => console.log(err));
  }, []);

  React.useEffect(() => {
    axios
      .get("/api/tags")
      .then((res) => setAllTags(res.data))
      .catch((err) => console.log(err));
  }, []);

  const getUserInfo = () => {
    const token = localStorage.getItem("REACT_TOKEN_AUTH_KEY");
    const my_jwt = token
      .split(":")[1]
      .substring(1, token.split(":")[1].length - 1);

    return axios
      .get("/api/protected", {
        headers: { Authorization: "Bearer " + my_jwt },
      })
      .then((res) => res.data);
  };

  function handleSubmit(e) {
    getUserInfo().then((userData) => {
      const data = {
        post: {
          user_id: userData.user_id,
          city_id,
          title,
          post_text,
          tags: [tag],
        },
      };
      axios
        .post("/api/posts", data)
        .then(() => {
          console.log("post add");
        })
        .catch((err) => console.log(err));
    });
  }

  return (
    <main>
      <form className="form" onSubmit={handleSubmit}>
        <div className="add_post">
          <h2 className="formTitle"> Add a new post </h2>
          <div className="inputBar">
            <input
              className="title formInput"
              type="text"
              placeholder="Add title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
            <label for="city-select" className="formLabel">
              Select the city:
            </label>
            <select
              className="formInput"
              id="city-select"
              value={city_id}
              onChange={(e) => setCity(e.target.value)}
            >
              {allCities.map((city) => (
                <option value={city.city_id} key={city.city_id}>
                  {city.city_name}
                </option>
              ))}
            </select>
            <label for="tag-select" className="formLabel">
              Select the applicable tag:
            </label>
            <select
              id="tag-select"
              className="formInput"
              value={tag}
              onChange={(e) => setTag(e.target.value)}
            >
              {allTags.map((tag) => (
                <option value={tag.tag_id} key={tag.tag_id}>
                  {tag.tag_name}
                </option>
              ))}
            </select>
          </div>
          <textarea
            className="typingArea"
            type="text"
            placeholder="What do you want to share?"
            value={post_text}
            onChange={(e) => setPost(e.target.value)}
            required>
          </textarea>
          <button className="post_button" type="submit">
            Add Post
          </button>
        </div>
      </form>
    </main>
  );
}
