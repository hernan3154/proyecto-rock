
document.addEventListener("DOMContentLoaded", function() {
    var passwordInputs = document.querySelectorAll('input[type="password"]');
    var toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(function(button, index) {
        button.addEventListener('click', function() {
            if (passwordInputs[index].type === "password") {
                passwordInputs[index].type = "text";
                toggleButtons[index].innerHTML = '<span class="far fa-eye"></span>';
            } else {
                passwordInputs[index].type = "password";
                toggleButtons[index].innerHTML = '<span class="far fa-eye-slash"></span>';
            }
        });
    });
});