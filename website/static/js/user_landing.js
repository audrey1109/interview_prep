/*
landing_page.js - audrey palmer

contains javascript for my users' landing page
*/

document.addEventListener("DOMContentLoaded", function() {
    const status = document.body.dataset.adminStatus;

    const admin_status = status === "true";
    
    if (admin_status) {
        let dashboard_link = document.getElementById("dashboard_link");
        dashboard_link.classList.remove("invisible");
    }
});

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