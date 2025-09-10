function log_out() {
    /// tells python to log the current user out
    fetch("/log_out", {
        method : "POST"
    })
    .then(response => response.json())
    .then(data => {
        if (data.case === "logged_out") {
            alert("log out successful! see you soon :D");
            window.location.href = "/";
        }
    });
}