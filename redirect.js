document.addEventListener("DOMContentLoaded", function () {
    const feedback_form = document.getElementById("feedback_form");
    const submit_button = document.getElementById("submit_button");

    feedback_form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Perform any form validation here if needed

        // Redirect to the thank you page
        window.location.href = "thankyou.html";
    });
});
