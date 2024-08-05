# Welcome to PP4: Learn English Online! 

For project four I decided to deveop a site for learners of English as a Foreign Language. I am currently working as an English Teacher at a college in Germany and thought an online resource for my students would be an interesting and fulfilling project to pursue. 

## Project Overview
This website is designed to allow Learners of English as a Foreign Language to create an account, make an online appointment with a tutor to discuss anything about the English language, and also practise some skills with our online games and exercises. This Minimum Viable Product (MVP) version has full 'Create - Read - Update - Delete' (CRUD) functionality in that the user can make an appointment, change the date, the time, or both the date and time of their appointment, or cancel the appointment altogether.

It built on the mobile-first principle around a Django framework in which I use Bootstrap elements to style the website and enhance the user experience across different browsers and devices. The front-end and back-end security is provided by the @login_required decorator along with CSRF protection implemented via the {% csrf_token %} template tag. It also has a basic admin interface in which the superuser has an overview of all users and appointments, can add language exercises, and can update or delete users, appointments and exercises as required.  

## Structure
The most important apps and folders are: 

- english_tutor: the main project app
- appointments: for booking and managing calls between the users and the tutors
- env.py: stores environment variables
- games_and_exercises: stores the online exercises
- home: the homepage
- Procfile_ specifies what commands are run when it starts 
- requirements.txt: lists project dependencies
- static and staticfiles: CSS, favicon, images, JS
- templates: base.html, 404.html, login.html, logout.html, signup.html
- user_accounts: stores user information at registration

## User Demographic
This game is aimed at learners of English as a foreign language of all ages. The exercises are set between the A2 and C1 levels; these levels are correspond to levels of language proficiency as defined by the Common European Framework of Reference for Languages (the CEFR). Broadly speaking, levels A - C equate to the following:  
- A: basic users
- B: intermediate users
- C: proficient users 

Each of these levels is divided into two subgroups to reflect progress in language learning. For the purposes of this project, I have provided exercises for the following groups: 
- A2
- B1
- B2
- C1

as these are the groups I am most familiar with. A future iteration could easily cover A1 and C2 students.

My students come from around the globe; while the majority are German, I have students from France, Italy, Latvia, Ukraine, Russia, Syria, Lebanon, Egypt, Algeria, Ghana, Mauritius, China, India, Pakistan, Malaysia, South Korea, Colombia, Mexico and so on. It is often the case that language learners from a particular groups struggle with different aspects of the English language; German speakers find the difference between the past simple and present perfect difficult, for example, whereas Russian and Arabic speakers need extra practise on when to use the definite and indefinite articles ('the' vs 'a / an' ). Learners of all languages find phrasal verbs and linking words challenging. So after teaching at this college for nearly five years, I have developed a decent grasp of what learners from each language group and level need. The exercises I have designed for this MVP are just the first step, and further iterations will both deepen and expand the offer to reflect this. 

More information about the CEFR can be found here: https://www.coe.int/en/web/common-european-framework-reference-languages/home

# UX and Design
Following the mobile-first approach of the Code Institute, as well as the educational purpose of the website itself, I have tried to keep the design and layout of this project as simple as possible. 

## Design
Some basic research showed me that educational or language learning-related websites utilise a mix of whites and blues / greens, e.g. [Grammarly](https://www.grammarly.com/), [the DeepL Translator](https://www.deepl.com/en/translator), and [DuoLingo](https://www.duolingo.com/learn). Related websites like [ChatGPT](https://chatgpt.com/) and [Google Translate](https://translate.google.com/?sl=de&tl=en&op=translate) follow a similar aesthetic, and this [Verpex Blog](https://verpex.com/blog/website-tips/best-color-combinations-for-educational-websites#) was very informative on the subject.

I therefore settled on a fairly muted mix of whites and blues to minimise distraction from the educational content, and to strike a professional tone with my audience. Duolingo is notably different in that it utilises a range of symbols and stickers to liven up progress, but in order to get my MVP ready for submission by the set deadline, I decided against adapting this much more challenging approach as it would require not only significantly better coding skills, but I suspect extensive market research and analysis of on-site user behaviour!  

## Text vs Images 
This website has fewer images than might be expected of a modern website. This is however deliberate. As the focus is on language practise, it is difficult to translate this into engaging images as is possible for, e.g. a food or travel site. There are some images, but I have kept them to a minimum to avoid distraction, and they seemed rather superfluous.  

## Homepage Explainers
I chose to add some explainers to the homepage for several reasons.  
- The card explainers: these cards appear at the top of the page and are small enough to give the visitor an 'at-a-glance' survey of the purpose of the website and what we offer. I chose to convey the information with Bootstrap Cards are the headers are concise, can be configured to give more information, and work well on mobile. 
- The accordion explainers: the feature: the accordion feature is similar to the cards in that it can convey precise information in an extremely concise way, doesn't take up too much room - so is excellent for mobile - and can expand for more information when necessary. 
- The accordion explainers: why give this information? English is very widely spoken, often to a decent standard, and during my teaching career I have often heard the question "Why must I bother with English, I can do it anyway!" My answer in those cases is to tie the language skills to particular purposes: yes, your English is good, but would you be comfortable leading a team or writing an essay or dissertation in English? What about doing a degree program in English, not just in an English-speaking country, but even in a coutry like Japan? And for everyone with a second or third language, there are always gaps to fill or things to improve. I have included this information to appeal not just to that sense of ambition to get better, but also to provide practical use-cases where better English skills will be a definite, practical benefit.    

Together, the card and accordion explainers should give the user a decent impression of what the site can offer, what they can do on the site and what benefit they will gain from interacting with it. This Bootstrap functions are also excellent for mobile devices, which is why I chose to go with them. 

## Registration page
The details requested of the user during the account registration is at an absolute minimum. The benefits of this approach are:
- it is easy for the user, which means it will convert a greater percentage of 'hit-and-run' visitors into actual site users
- in a post-mvp world, I will enable a 'user portal' where regular users can add personal details, if they wish 
- security: the less information a website holds the better. Hacking and / data leaks (intentional or not) are an ever-present risk, so I prefer websites which ask for less personal and sensitive information over those which request more than the bare minimum.  


# Database overview

## User Information Model
This is captured at the user-registration page and stored in the user_accounts app -> model.py
In the future, this will be the basis for the user account section, where the User will be the ForeignKey around which other information will be arranged. It captures information for username, email and password. For the purposes of this MVP, the name and surname fields are present in the model, but I have not yet provided a field for the user to enter the. In the future, this will happen in the 'user account' section which is not yet implemented.  

## Appointments Model
This is stored in the appointments app -> models.py. The user_profile captured at registration is the ForeignKey as the core of a one-to-many relationship. At this stage, the model also captures meeting date and time, a message provided by the user, and a hidden created_on = models.DateTimeField field.  

**Form Validation and Constraints.** I have implemented the following validations and constraints on the appointments model by implementing the Django 'clean' method.  

Variables explanation: 
- min_date: this is designed to ensure that appointments can only be made in the future, to avoid unintentional / intentional appointments in the past.
- max_date: in order to keep the overview of the appointments, users can only book up to 4 weeks in advance. This variable is easily changed.
- meeting_duration: appointments are advertised as 30 minutes, but I have set up a 40 minute block to give the tutor a buffer between meetings. This variable also helps avoid meeting overlap (see below) and can be easily changed.  
- meeting_start and meeting_end: based on the meeting_duration, this tracks what block of time should be marked as 'unavailable' for when other users attempt to make appointments.
- overlapping_appointments: when a user books an appointment, this is run in order to identify if another meeting is in place during this booking request.  

In each of the above cases, error messages are shown to the user to alert them to the problem:
- Please check your appointment date: your appointment must be between {min_date} and {max_date}
- Please choose a different time. Our appointments run between {MORNING_START_TIME.strftime('%H:%M')} and {MORNING_END_TIME.strftime('%H:%M')}
- "This appointment slot is unavailable. Please choose a different time."