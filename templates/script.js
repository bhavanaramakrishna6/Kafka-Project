let user = localStorage.getItem("user");

if (!user) {
    user = prompt("Enter your username:");
    localStorage.setItem("user", user);
}

// Load or initialize logs
let logs = JSON.parse(localStorage.getItem("logs")) || [];

// Load counts
let counts = JSON.parse(localStorage.getItem("counts")) || {
    home: 0,
    product: 0,
    cart: 0,
    checkout: 0,
    nav_home: 0,
    nav_product: 0,
    nav_cart: 0
};

function sendClick(page) {
    const time = new Date().toLocaleString();

    // Update counts
    if (!counts[page]) counts[page] = 0;
    counts[page]++;

    // Save log entry
    logs.push({
        user: user,
        page: page,
        time: time
    });

    // Save to localStorage
    localStorage.setItem("logs", JSON.stringify(logs));
    localStorage.setItem("counts", JSON.stringify(counts));

    // Send to backend
    fetch("http://localhost:5000/click", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user: user, page: page })
    }).catch(err => console.log("Backend not running:", err));
}

// Show username in navbar
document.addEventListener("DOMContentLoaded", () => {
    const userDisplay = document.getElementById("userDisplay");
    if (userDisplay) {
        userDisplay.innerText = "Logged in as: " + user;
    }
});

// Apply saved theme on load
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        document.body.classList.add("light");
    }
});

// Toggle theme
function toggleTheme() {
    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {
        localStorage.setItem("theme", "light");
    } else {
        localStorage.setItem("theme", "dark");
    }
}
