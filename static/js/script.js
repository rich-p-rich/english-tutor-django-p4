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

// Register and login page: the 'show password' toggle functionality 
function togglePassword(fieldId) {
    var x = document.getElementById(fieldId);
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

// Games and Exercises page: dropdown menu to filter language difficulty level
function filterQuestions(level) {
    const quizzes = document.querySelectorAll('.quiz');
    quizzes.forEach(quiz => {
        if (level === 'all' || quiz.id.startsWith(level)) {
            quiz.classList.remove('hidden');
        } else {
            quiz.classList.add('hidden');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    filterQuestions();
});

/* Games and Exercises page: the function to set the selected difficulty level */
function setDifficulty(level) {
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => {
        if (level === 'all' || content.getAttribute('data-difficulty') === level) {
            content.style.display = 'block';
        } else {
            content.style.display = 'none';
        }
    });
} 

// Games and Exercises pages: show language section
function showHideSection() {
  document.getElementById("game-rules").classList.toggle("hide");
}

// Games and Exercises pages: check answer and feedback
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const questions = document.querySelectorAll('li[id]');
        questions.forEach(question => {
            const selectedOption = question.querySelector('input[type="radio"]:checked');
            const feedback = question.querySelector('.feedback');
            
            if (selectedOption) {
                const isCorrect = selectedOption.getAttribute('data-correct') === 'true';
                if (isCorrect) {
                    feedback.textContent = 'Correct!';
                    feedback.style.color = 'green';
                } else {
                    feedback.textContent = 'Incorrect!';
                    feedback.style.color = 'red';
                }
            } else {
                feedback.textContent = 'Please select an answer.';
                feedback.style.color = 'orange';
            }
        });
    });
});
