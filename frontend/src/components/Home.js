import "./style/Home.css";
import { useAuth } from "../auth";
import Login from "./Login";

function Home() {
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
    //console.log(opts)
    fetch("/api/protected", {
      method: "get",
      headers: {
        Authorization: "Bearer " + my_jwt,
      },
    })
      .then((r) => r.json())
      .then((rJson) => console.log(rJson));
  };

  return (
    <div className="Home">
      <p> This is your home!</p>
      <button onClick={onSubmitClick}> check </button>
    </div>
  );
}

export default Home;
