import "./style/Dashboard.css";
import Post from "./Post.js";
import Elem from "./RenderElem.js";
import Addposts from "./Addposts.js";
import Login from "./Login";
import { useAuth } from "../auth";
import "./style/Tags.css";

function Dashboard() {
  const [logged] = [useAuth()];

  if (!logged[0]) {
    return <Login />;
  }
  return (
    <div className="Dashboard">
      <div className="App-header">
        <div className="AppMenu">
          <Addposts />
          <Elem
            path="/api/cohorts"
            title="Cohorts"
            tagName="cohort_name"
          ></Elem>
          <Elem path="/api/tags" title="Tags" tagName="tag_name"></Elem>
        </div>
        <div className="AppContent">
          <Post />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
