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

// Toggle show password functionality on log-in page 

function togglePassword () {
    var x = document.getElementById("passwordInput")
    if (x.type === "password") {
        x.type = "text";
    } else {
      x.type = "password";
    }
}