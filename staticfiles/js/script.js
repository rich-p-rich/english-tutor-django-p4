//The cancellation modal in change-or-cancel.html

document.addEventListener('DOMContentLoaded', function () {
    var cancelModal = document.getElementById('cancelModal');
    cancelModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var appointmentId = button.getAttribute('data-appointment-id');
        var modalBodyInput = cancelModal.querySelector('.modal-footer input[name="appointment_id"]');
        modalBodyInput.value = appointmentId;
    });
});

// Toggle show password functionality on register and login pages
function togglePassword(fieldId) {
    var x = document.getElementById(fieldId);
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

// Function to set the selected difficulty level
function setDifficulty(level) {
    document.getElementById('difficulty').value = level;
    filterQuestions();
}

// Dropdown menu to filter language difficulty level
function filterQuestions() {
    var selectedLevel = document.getElementById('difficulty').value;
    var questions = document.querySelectorAll('.question');

    questions.forEach(function(question) {
        if (selectedLevel === 'all' || question.getAttribute('data-language-level') === selectedLevel) {
            question.classList.remove('hidden');
        } else {
            question.classList.add('hidden');
        }
    });
}
filterQuestions();
