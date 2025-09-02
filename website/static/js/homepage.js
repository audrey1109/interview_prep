
// LISTENERS ----------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    // this means theyre listening as soon as the page loads
        document.getElementById("comment_collection").addEventListener("input", function() {

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