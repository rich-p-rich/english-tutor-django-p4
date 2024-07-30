{% load static %}

{% url 'home' as home_url %}
{% url 'account_login' as login_url %}
{% url 'account_signup' as signup_url %}
{% url 'account_logout' as logout_url %}

<!DOCTYPE html>
<html class="h-100" lang="en">

<head>
  <title>{% block title %}English Tuition Online | Boost your English Language Skills{% endblock %}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
  <!--Bootstrap CSS-->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
  <!--Fontawesome-->
  <script src="https://kit.fontawesome.com/7a1565e963.js" crossorigin="anonymous"></script>
  <!--Custom CSS-->
  <link rel="stylesheet" href="/static/css/style.css" type="text/css" />


  <!--Favicon-->
  <link rel="apple-touch-icon" sizes="180x180" href="{% static 'favicon/apple-touch-icon.png' %}">
  <link rel="icon" type="image/png" sizes="32x32" href="{% static 'favicon/favicon-32x32.png' %}">
  <link rel="icon" type="image/png" sizes="16x16" href="{% static 'favicon/favicon-16x16.png' %}">
</head>

<body id="body" class="d-flex flex-column h-100 main-bg">
  <header>
    <h1 class="header-home">Learn English Online</h1>
    <h2 class="header-home">For Learners of English as a Foreign Language</h2>
  </header>
  <!-- Navigation -->
  <nav id="navbar" class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'homepage' %}">Home</a>
          </li>
          {% if user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link {% if request.path == logout_url %}active{% endif %}" aria-current="page"
              href="{% url 'account_logout' %}">Logout</a>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link {% if request.path == signup_url %}active{% endif %}" aria-current="page"
              href="{% url 'account_signup' %}">Register</a>
          </li>
          <li class="nav-item">
            <a class="nav-link {% if request.path == login_url %}active{% endif %}" aria-current="page"
              href="{% url 'account_login' %}">Login</a>
          </li>
          {% endif %}
          {% if user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'appointments' %}">Book a call</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'change_appointments' %}">Change your appointment</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{% url 'all_exercises' %}" id="navbarDropdownMenuLink"
              role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Games and Exercises</a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="{% url 'section_list' 'A2' %}">A2 Level</a></li>
              <li><a class="dropdown-item" href="{% url 'section_list' 'B1' %}">B1 Level</a></li>
              <li><a class="dropdown-item" href="{% url 'section_list' 'B2' %}">B2 Level</a></li>
              <li><a class="dropdown-item" href="{% url 'section_list' 'C1' %}">C1 Level</a></li>
              <li><a class="dropdown-item" href="{% url 'section_list' 'All' %}">All</a></li>
            </ul>
          </li>
          {% else %}
          <div class="modal fade" id="authModal" tabindex="-1" aria-labelledby="authModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="authModalLabel">Welcome!</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <p>Please register or log in to continue using the website.</p>
                  <div class="d-flex justify-content-around">
                    <a href="{% url 'account_signup' %}" class="btn btn-primary">Register</a>
                    <a href="{% url 'account_login' %}" class="btn btn-secondary">Log In</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {% endif %}
          <li class="nav-item">
            <a class="nav-link" href="#">About Us</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Message to confirm logon status -->
  <main class="flex-shrink-0 main-bg">
    <div id="login-status">
      {% if user.is_authenticated %}
      <p class="text-end m-3">Welcome {{ user.username }}</p>
      {% else %}
      <p class="text-end m-3">You are not logged in</p>
    </div>
    {% endif %}

    <main class="flex-shrink-0 main-bg">

      {% block content %}
      <!-- Content Goes here -->
      {% endblock content %}

    </main>

    <!-- Footer -->
    <footer>
      <ul id="social-networks">
        <li>
          <a href="https://www.instagram.com/" target="_blank" rel="noopener"
            aria-label="Visit our Instagram page (opens in a new tab)"><i class="fa-brands fa-instagram"></i></a>
        </li>
        <li>
          <a href="https://www.youtube.com" target="_blank" rel="noopener"
            aria-label="Visit our YouTube page (opens in a new tab)"><i class="fa-brands fa-youtube-square"></i></a>
        </li>
        <li>
          <a href="https://www.facebook.com" target="_blank" rel="noopener"
            aria-label="Visit our Facebook page (opens in a new tab)"><i class="fa-brands fa-facebook"></i></a>
        </li>
      </ul>
    </footer>

    <!--Bootstrap JS CDN-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <!--Script.JS-->
    <script src="/static/js/script.js"></script>