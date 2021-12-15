import React from "react";
import axios from "axios";
import "./Addposts.css";

export default function Addposts() {
  const [city_id, setCity] = React.useState(1);
  const [edited, setEdit] = React.useState(false);
  const [post_text, setPost] = React.useState("");
  const [title, setTitle] = React.useState("");
  const [upvotes, setUpvote] = React.useState(0);
  const [user_id, setUser] = React.useState("");

  const [allCities, setAllCities] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/cities")
      .then((res) => setAllCities(res.data))
      .catch((err) => console.log(err));
  }, []);

  function handleSubmit(e) {
    const created_at = new Date().toISOString();
    const submit = {"post": 
    {user_id,
    city_id,
    title,
    post_text
}
    };

    axios.post("http://127.0.0.1:5000/api/posts", submit).then(() => {
      console.log("post add");
    });

    // fetch("http://127.0.0.1:5000/posts",{
    //     method:'POST',
    //     headers: {"Content-Type": "application/json"},
    //     body: JSON.stringify(submit)
    // }).then(() => {
    //     console.log('new post added')
    //     console.log(submit)
    // })
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

          {/* axios.map */}
          <select value={city_id} onChange={(e) => setCity(e.target.value)}>
            {allCities.map((city) => (
              <option value={city.city_id}>{city.city_name}</option>
            ))}
          </select>

          <button className="post_button" type="submit">Add Post</button>
        </div>
      </form>
    </main>
  );
}
