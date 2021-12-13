import React from "react"

export default function Addposts(){
    function handleClick(){
        console.log('I was clicked!')

    }
    return (
        <main >
            const result = React.useState()
            console.log(result)
            <form className="form">
                <input className="input"
                    type="text"
                    placeholder="Share with Minervans!"
                />
                <button onClick={handleClick}>Add Post</button>
            </form>
        </main>
    )
}