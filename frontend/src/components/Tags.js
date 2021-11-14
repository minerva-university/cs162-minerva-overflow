import useSWR from "swr";

function Tags() {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const api_url = "https://minerva-overflow.herokuapp.com/tags";
  const { data, error } = useSWR(api_url, fetcher);

  if (error) {
    console.log(error);
    return <div>error</div>;
  }
  if (!data) return <div>loading...</div>;

  // render data
  return <div>hello {data}!</div>;
}

export default Tags;
