<div class="container">
    <h1>{{ level }} Level Exercises</h1>
    <form method="post">
        {% csrf_token %}
        {% if level == "A2" %}
            {% include "partials/_a2_exercises.html" %}
        {% elif level == "B1" %}
            {% include "partials/_b1_exercises.html" %}
        {% elif level == "B2" %}
            {% include "partials/_b2_exercises.html" %}
        {% elif level == "C1" %}
            {% include "partials/_c1_exercises.html" %}
        {% endif %}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>



<div class="container">
    <h1 class="text-center">Games and Exercises</h1>
    <p>Welcome to our test and exercises to help you practise your English.</p>
    <p>Choose your difficulty level from the drop-down menu to set the right exercises for you:</p>
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
            data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><button class="dropdown-item" type="button" onclick="setDifficulty('A2')">A2 exercises</button></li>
            <li><button class="dropdown-item" type="button" onclick="setDifficulty('B1')">B1 exercises</button></li>
            <li><button class="dropdown-item" type="button" onclick="setDifficulty('B2')">B2 exercises</button></li>
            <li><button class="dropdown-item" type="button" onclick="setDifficulty('C1')">C1 exercises</button></li>
            <li><button class="dropdown-item" type="button" onclick="setDifficulty('all')">All exercises</button></li>
        </ul>
    </div>
    <!-- Hidden input to store selected difficulty -->
    <input type="hidden" id="difficulty" value="all">
    <!-- Exercise questions -->
    <div class="content" data-difficulty="A2">
        <p>A2 Exercises</p>
    </div>
    <div class="content" data-difficulty="B1">
        <p>B1 exercises</p>
    </div>
    <div class="content" data-difficulty="B2">
        <p>B2 exercises</p>
    </div>
    <div class="content" data-difficulty="C1">
        <p>C1 exercises</p>

        <div id="C1-linking-words-quiz-1">
            <h5>C1: Linking Words Quiz</h5>
        <p>Complete the following sentences by choosing from the options below.</p>
        <ol>
            <li>
                <p>______ the weather was terrible, we decided to go hiking anyway.</p>
                <form id="c1-lw-quiz-1">
                    <!-- Name attribute explanation: c1-lw-choice-1: C1 level, Linking Words, Choice 1, etc -->
                    <input type="radio" name="c1-lw-choice-1" value="Because" data-correct="false"> Because<br>
                    <input type="radio" name="c1-lw-choice-1" value="Despite" data-correct="false"> Despite<br>
                    <input type="radio" name="c1-lw-choice-1" value="Although" data-correct="true"> Although<br>
                </form>
                <button onclick="submitAnswer('c1-lw-quiz-1')">Submit Answer</button>
                <p class="feedback"></p>
            </li>
            <li>
                <p>The project was completed on time ______ we faced numerous delays and challenges.</p>
                <form id="c1-lw-quiz-2">
                    <input type="radio" name="c1-lw-choice-2" value="even though" data-correct="true"> even though<br>
                    <input type="radio" name="c1-lw-choice-2" value="as" data-correct="false"> as<br>
                    <input type="radio" name="c1-lw-choice-2" value="despite" data-correct="false"> despite<br>
                </form>
                <button onclick="submitAnswer('c1-lw-quiz-2')">Submit Answer</button>
                <p class="feedback"></p>
            </li>
            <li>
                <p>The new policy was implemented ______ improve efficiency and has been extremely successful.</p>
                <form id="c1-lw-quiz-3">
                    <input type="radio" name="c1-lw-choice-3" value="in order to" data-correct="true"> in order to<br>
                    <input type="radio" name="c1-lw-choice-3" value="so that" data-correct="false"> so that<br>
                    <input type="radio" name="c1-lw-choice-3" value="because" data-correct="false"> because<br>
                </form>
                <button onclick="submitAnswer('c1-lw-quiz-3')">Submit Answer</button>
                <p class="feedback"></p>
            </li>
        </ol>
    </div>