import React from "react"
import axios from "axios";
import "./Addposts.css"

export default function Addposts(){
    const [city_id, setCity] = React.useState(1);
    const [edited, setEdit] = React.useState(false);
    const [post_text, setPost] = React.useState("")
    const [title, setTitle] = React.useState('');
    const [upvotes, setUpvote] = React.useState(0);
    const [user_id, setUser] = React.useState("");

    function handleSubmit(e){
        e.preventDefault();
        const created_at = new Date().toISOString();
        const submit = {
            city_id,
            created_at,
            edited,
            post_text,
            title,
            upvotes,
            user_id,
        };

       
        axios.post("http://127.0.0.1:5000/api/posts",submit)
            .then(() => {console.log("post add")})
            
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
        <main >
            <form className="form" onClick={handleSubmit}>
                <div className="add_post">
                    <input className="title"
                        type="text"
                        placeholder="Add title"
                        value={title}
                        onChange={(e)=>setTitle(e.target.value)}
                        required
                    />

                    <input className="input"
                        type="text"
                        placeholder="What do you want to share with Minervans?"
                        value={post_text}
                        onChange={(e)=>setPost(e.target.value)}
                        required
                    />
                    <button className="post_button"
                    >Add Post</button>

                    {/* axios.map */}
                    <select value={city_id} onChange={(e)=>setCity(e.target.value)}>
                        <option value="1">San Francisco</option>
                        <option value="2">Seoul</option>
                        <option value="3">Hyderabad</option>
                        <option value="4">Berlin</option>
                        <option value="5">Buenos Aires</option>
                        <option value="6">London</option>
                        <option value="7">Taipei</option>
                    </select>
                </div>
            </form>
        </main>
    )
}