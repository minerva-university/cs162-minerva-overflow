import React, { useState, useEffect } from "react";
import "./style/Tags.css";

function Elem(prop) {
  //Used to render tag element
  const [elements, setElements] = useState(["loading..."]);
  useEffect(() => {
    fetch(prop.path, { method: "get" })
      .then((response) => {
        if (response.status === 401) {
          setElements(["Sorry you aren't authorized!"]);
          return null;
        }
        return response.json();
      })
      .then((response) => {
        if (response) {
          setElements(response.map((tag) => tag[prop.tagName]));
        }
      });
  }, []);

  const listItems = elements.map((e, i) => (
    <p className="Button" key={i}>
      {e}
    </p>
  ));
  return (
    <div className="TagContainer">
      <div className="TagTitle">{prop.title}</div>
      <div className="Tags">{listItems}</div>
    </div>
  );
}

export default Elem;
