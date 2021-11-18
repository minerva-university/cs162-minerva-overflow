import React, { useState, useEffect } from "react";

function Elem(prop) {
  const [elements, setElements] = useState("loading...");
  useEffect(() => {
    fetch(prop.path)
      .then((res) => res.json())
      .then((data) => {
        setElements(data.map((obj) => obj[prop.tagName]));
      });
  }, []);
  console.log(elements);
  const listItems = elements.map((e) => <p className="Button">{e}</p>);
  return (
    <div>
      <p>{listItems}</p>
    </div>
  );
}

export default Elem;
