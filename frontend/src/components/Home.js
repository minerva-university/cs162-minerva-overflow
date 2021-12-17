import "./style/Home.css";
import "./style/Addposts.css";
import { useAuth } from "../auth";
import Login from "./Login";
import { useState } from "react";

function Home() {
  const [info, setInfo] = useState([]);
  const [show, setShow] = useState(false);

  const [logged] = [useAuth()];
  if (!logged[0]) {
    return <Login />;
  }

  const token = localStorage.getItem("REACT_TOKEN_AUTH_KEY");
  const my_jwt = token
    .split(":")[1]
    .substring(1, token.split(":")[1].length - 1);

  const onSubmitClick = (e) => {
    e.preventDefault();
    // console.log(opts)
    fetch("/api/protected", {
      method: "get",
      headers: {
        Authorization: "Bearer " + my_jwt,
      },
    })
      .then((r) => r.json())
      .then((res) => setInfo(res))
      .then((rJson) => console.log(rJson))
      .then(setShow(true));
  };

  return (
    <div className="Home">
      <h1> Welcome back to Minerva Overflow!</h1>
      <button className="post_button" onClick={onSubmitClick}>
        {" "}
        Show user detail{" "}
      </button>
      <button className="post_button" onClick={() => setShow(false)}>
        {" "}
        Hide{" "}
      </button>
      {show ? (
        <div>
          <p>First name: {info.first_name}</p>
          <p>Surname: {info.surname}</p>
          <p>Username: {info.username}</p>
          <p>Email: {info.email}</p>
          <p>About Me: {info.about_me}</p>
          <p>Cohort: {info.cohort_id}</p>
        </div>
      ) : null}
    </div>
  );
}

export default Home;
