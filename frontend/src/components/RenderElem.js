import React, { useState, useEffect } from "react";

function Elem(prop) {
  const [elements, setElements] = useState(["loading..."]);
  useEffect(() => {
    fetch(prop.path)
      .then((res) => res.json())
      .then((data) => {
        setElements(data.map((obj) => obj[prop.tagName]));
      });
  }, []);
  const listItems = elements.map((e) => <p className="Button">{e}</p>);
  return (
    <div className="TagContainer">
      <div>{prop.path}</div>
      <div className="Tags">{listItems}</div>
      {/* {console.log(typeof elements == typeof [])} */}
    </div>
  );
}

export default Elem;
