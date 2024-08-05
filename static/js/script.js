// Register page: the 'show password' toggle functionality
function togglePassword(fieldId) {
    var x = document.getElementById(fieldId);
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

// Add custom validation messages to Registration and Login
// registration form: templates/account/signup-html
// login form: templates/account/login.html
document.addEventListener('DOMContentLoaded', function () {
    // Select all forms with the class 'needs-validation'
    const forms = document.querySelectorAll('form.needs-validation');

    forms.forEach((form) => {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            // Apply custom validation feedback to all fields except for submit button
            Array.from(form.elements).forEach((input) => {
                if (input.type !== "submit") {
                    let feedback = input.closest('.form-group')?.querySelector('.invalid-feedback');

                    if (feedback) {
                        if (input.checkValidity() === false) {
                            if (input.validity.valueMissing) {
                                feedback.textContent = `The ${input.name} field is required.`;
                            } else if (input.validity.typeMismatch) {
                                feedback.textContent = `Please enter a valid ${input.type}.`;
                            } else if (input.validity.tooShort) {
                                feedback.textContent = `The ${input.name} needs to be at least ${input.minLength} characters; you entered ${input.value.length}.`;
                            }

                            input.classList.add('is-invalid');
                        } else {
                            input.classList.remove('is-invalid');
                            feedback.textContent = '';
                        }
                    }
                }
            });

            form.classList.add('was-validated');
        }, false);
    });
});


// Homepage: signin modal from the explanation cards
document.addEventListener('DOMContentLoaded', () => {
    const bookCallLink = document.getElementById('bookCallLink');
    const exercisesLink = document.getElementById('exercisesLink');

    if (!bookCallLink && !exercisesLink) {
        return;
    }

    const handleLinkClick = (event) => {
        const link = event.currentTarget;
        const isAuthenticated = link.dataset.isAuthenticated === 'true';
        const loginUrl = link.dataset.loginUrl;
        const registerUrl = link.dataset.registerUrl;
        const targetUrl = link.dataset.appointmentsUrl || link.dataset.games_and_exercisesUrl;
        const signInModal = new bootstrap.Modal(document.getElementById('signInModal'));

         if (!isAuthenticated) {
            event.preventDefault();
            signInModal.show();

            document.getElementById('loginButton').addEventListener('click', () => {
                window.location.href = loginUrl;
            });

            document.getElementById('registerButton').addEventListener('click', () => {
                window.location.href = registerUrl;
            });
        } else {
            window.location.href = targetUrl;
        }
    };

    if (bookCallLink) {
        bookCallLink.addEventListener('click', handleLinkClick);
    }

    if (exercisesLink) {
        exercisesLink.addEventListener('click', handleLinkClick);
    }
});

// Appointments page: set appointment ID
function setAppointmentId(id) {
    document.getElementById('appointment_id').value = id;
}

// Games and Exercises pages: show language section
function submitAnswer(questionId) {
    const question = document.getElementById(questionId);
    if (!question) {
        console.error(`Element with ID ${questionId} not found.`);
        return;
    }

    const selectedOption = question.querySelector('input[type="radio"]:checked');
    const feedback = question.querySelector('.feedback');

    if (selectedOption) {
        // Get the value of the data-correct attributes
        const isCorrect = selectedOption.getAttribute('data-correct') === 'True' || selectedOption.getAttribute('data-correct') === 'true';
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
}

// Event listener for the Exercise Form -> games_and_exercises/templates/question-list
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('exercises');
   
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const questions = document.querySelectorAll('li[id^="question-"]');
            questions.forEach(question => {
                submitAnswer(question.id);
            });
        });
    } 
});