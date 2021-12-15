import React from "react";
import axios from "axios";
import "./style/Addposts.css";

export default function Addposts() {
  const [city_id, setCity] = React.useState(1);
  const [post_text, setPost] = React.useState("");
  const [title, setTitle] = React.useState("");

  const [allCities, setAllCities] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/cities")
      .then((res) => setAllCities(res.data))
      .catch((err) => console.log(err));
  }, []);

  function handleSubmit(e) {
    const user_id = 1;
    const data = { post: { user_id, city_id, title, post_text } };

    axios
      .post("/api/posts", data)
      .then(() => {
        console.log("post add");
      })
      .catch((err) => console.log(err));
  }

  return (
    <main>
      <form className="form" onSubmit={handleSubmit}>
        <div className="add_post">
          <input
            className="title"
            type="text"
            placeholder="Add title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />

          <input
            className="input"
            type="text"
            placeholder="What do you want to share with Minervans?"
            value={post_text}
            onChange={(e) => setPost(e.target.value)}
            required
          />

          <select value={city_id} onChange={(e) => setCity(e.target.value)}>
            {allCities.map((city) => (
              <option value={city.city_id}>{city.city_name}</option>
            ))}
          </select>

          <button className="post_button" type="submit">
            Add Post
          </button>
        </div>
      </form>
    </main>
  );
}
