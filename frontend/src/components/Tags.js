import { useState, useEffect } from "react";
import axios from "axios";
import "./style/Tags.css";

function Tags() {
  //a simple component used to display a tag
  const [allTags, setAllTags] = useState([]);

  useEffect(() => {
    axios
      .get("/api/tags")
      .then((res) => setAllTags(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      {" "}
      {allTags.map((tag) => (
        <div> #{tag.tag_name}</div>
      ))}
    </div>
  );
}

export default Tags;
