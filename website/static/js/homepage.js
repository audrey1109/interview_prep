
// LISTENERS ----------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {


    // shows comments
    // let comments = JSON.parse(document.getElementById("pagedata").dataset.comments);
    let rawComments = document.getElementById("pagedata").dataset.comments;
    console.log("Raw comments:", rawComments);
    let comments = JSON.parse(rawComments);
    console.log("Parsed comments:", comments);
    // console.log(comments);
    for (let i = 0; i < comments.length; i++) {
        console.log(comments[i]);
    }
    let com_container = document.getElementById("com_continer");
    com_container.classList.remove("invisible");

    if (comments.length != 0 ) {

        // let com_container = this.documentElement("com_continer");

        for (let i = 0; i < comments.length; i++) {

            const element = document.createElement("p");
            element.textContent = comments[i];

            com_container.appendChild(element);
        }
    } else {

        const element = document.createElement("p");
        element.textContent = "failure";
        com_container.appendChild(element);
    }
    

    document.getElementById("comment_collection").addEventListener("input", function() {
        // determins whether or not the button is enabled
        let text_len = this.value.length;

        if (text_len == 0 ) {
        document.getElementById("comment_submission").disabled = true;
        } else {
        document.getElementById("comment_submission").disabled = false;
        }})
})

// FUNCTIONS --------------------------------------------------------------------

function get_comment() {

    let comment = document.getElementById("comment_collection").value;

    fetch("/submit_comment", {

        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify({
            comment : comment
        })
    })

    .then(response => response.json())
    .then(data => {
        console.log("server response : ", data);
        document.getElementById("thanks").classList.remove("invisible");
    })
    .catch(error => {
        console.error("error! : ", error);
    });

}