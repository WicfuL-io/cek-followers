function openModal(id) {
    document.getElementById(id).classList.add("active");
}

function closeModal(id) {
    document.getElementById(id).classList.remove("active");
}

function filterList(input) {
    const value = input.value.toLowerCase();
    const users = input.parentElement.querySelectorAll(".user");

    users.forEach(u => {
        u.style.display = u.textContent.includes(value) ? "block" : "none";
    });
}
