import React from "react"

export default function Addposts(){
    function handleClick(){
        console.log('I was clicked!')

    }
    return (
        <main >
            <form className="form">
                <div class="add_post">
                    <div>
                        <textarea className="input"
                        type="text"
                        placeholder="Share with Minervans">

                        </textarea>
                    </div>
                    <div>
                        <button class="post_button" onClick={handleClick}>Post</button>
                    </div>
                </div>
            </form>
            
        </main>
    )
}