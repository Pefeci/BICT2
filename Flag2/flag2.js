url = "http://192.168.56.102"

async function authenticate(username, password){
        // Send a POST request to the backend for authentication
        await fetch(url + ":5000/authenticate", {
            method: "POST",
            body: JSON.stringify({ username, password }),
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Authentication successful, redirect to a new page
                window.location.href = url + ":80/" + data.url;
            } else {
                // Authentication failed, display an error message
                document.getElementById("message").textContent = "Authentication failed. Please try again.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("message").textContent = "An error occurred. Please try again.";
        });

}



document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    console.log(JSON.stringify({username, password}));
    authenticate(username, password);
});


