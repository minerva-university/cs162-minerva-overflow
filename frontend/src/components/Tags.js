import { useState, useEffect } from "react";
import axios from "axios";
function Tags() {
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
