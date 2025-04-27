document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll("ul li");

    items.forEach(item => {
        item.addEventListener("click", () => {
            alert("You clicked on: " + item.textContent);
        });
    });
});



document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("clientForm");

    form.addEventListener("submit", (e) => {
        const inputs = form.querySelectorAll("input");
        let valid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = "red";
                valid = false;
            } else {
                input.style.borderColor = "#ccc";
            }
        });

        if (!valid) {
            e.preventDefault();
            alert("Please fill in all the fields before submitting.");
        }
    });
});



document.addEventListener("DOMContentLoaded", () => {
    const programForm = document.getElementById("programForm");

    if (programForm) {
        programForm.addEventListener("submit", (e) => {
            const input = programForm.querySelector("input");
            if (!input.value.trim()) {
                e.preventDefault();
                input.style.borderColor = "red";
                alert("Please enter a program name before submitting.");
            }
        });
    }
});




document.addEventListener("DOMContentLoaded", () => {
    const enrollForm = document.getElementById("enrollForm");

    if (enrollForm) {
        enrollForm.addEventListener("submit", (e) => {
            const selects = enrollForm.querySelectorAll("select");
            let valid = true;

            selects.forEach(select => {
                if (!select.value) {
                    select.style.borderColor = "red";
                    valid = false;
                } else {
                    select.style.borderColor = "#ccc";
                }
            });

            if (!valid) {
                e.preventDefault();
                alert("Please select both a client and a program.");
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("enrollForm");
    form.addEventListener("submit", () => {
        alert("Enrollment submitted successfully! 🎉");
    });
});

