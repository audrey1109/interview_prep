
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