import React from "react";
import "./style/Addposts.css";

export default function Addposts(){
    function handleClick(){
        console.log('I was clicked!')

    }
    return (
        <main>
            <form className="add_post">
                <textarea className="input" type="text"
                placeholder="Ask for a recommendation (e.g. Where can I find the best croissant in London?)">
                </textarea>
                <div>
                    <button className="post_button" onClick={handleClick}>Post</button>
                </div>
            </form>
            
        </main>
    )
}