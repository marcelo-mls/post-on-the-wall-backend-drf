<h1>Post on the Wall - Backend (Django)
  <img align="center" alt="python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
  <img align="center" alt="django" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg">
</h1>

> This is a backend part of a Full Stack application.

<br />

Link to application frontend:
- Frontnd with `React`: [post-on-the-wall/frontend/react](https://github.com/marcelo-mls/post-on-the-wall-frontend/tree/main)

<br />

Link to another backend option to this application:
- Backend with `Node.js`: [post-on-the-wall/backend/node](https://github.com/marcelo-mls/post-on-the-wall-backend-node/tree/main)
> one option excludes the other


## Description

This is an application that allows users to register, login and write a post on a wall.

Anonymous users can see all wall posts.

To write a post on the wall, the user needs to login.

<details>
  <summary>
  
  ### Built With
  </summary>
  
  For the development of this API was chosen [`Django`](https://www.djangoproject.com/), [`Django Rest Framework`](https://www.django-rest-framework.org/) and [`SQLite`](https://sqlite.org/index.html). Together, these technologies provide ...
  
  <img height="60" align="left" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg">
  <p align="rigth">Django</p>

  <img height="60" align="left" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
  <p align="rigth">Django Rest Framework</p>

  <img height="45" align="left" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg">
  <p align="rigth">SQLite</p>
 
  
  
</details>

## How to Install

These instructions will provide you a complete copy of the project up and running on your local machine for development purposes.

1. Clone the repository:
```sh
git clone git@github.com:marcelo-mls/post-on-the-wall-backend-drf.git
```

2. Enter the repository folder you just cloned:
```sh
cd post-on-the-wall-backend-drf
```

3. Install the dependencies and start the project:
```sh
pip install ...
django ...
```
<details>
  <summary>
  
  ## Routes
</summary>

  You can test the API with softwares like [`Insomnia`](https://insomnia.rest/download), [`Postman`](https://www.postman.com/) or [`Thunder Client`](https://www.thunderclient.com/)
  
  #### Django Rest Framework Interface
  - [Link]()

  #### Users:
  - GET: `'/user'` lists all users.
  - POST: `'/auth/user'` get a user by email. Auth token required.
  - POST: `'/user'` create a new user.
  - DELETE: `'/user/:id'` delete a user.

  #### Posts:
  - GET: `'/posts'` lists all posts.
  - POST: `'/posts'` create a new post. Auth token required.
  - DELETE: `'/posts/:id'` delete a user. Auth token required.
</details>

<details>
  <summary>
  
  ## Demonstration
  </summary>

  :warning: To have this view it is necessary to install and run the [frontend](https://github.com/marcelo-mls/post-on-the-wall-frontend/tree/main)
  
  - #### Guest view
  ![Guest view](https://user-images.githubusercontent.com/102492818/226949985-6ce05fd8-0dc7-494a-97c9-21d841132d40.png)

  - #### Login/Signup
  https://user-images.githubusercontent.com/102492818/226954914-a61bbcb8-246a-40d8-b18f-c26d79b9c572.mp4

  - #### Authed user view
  https://user-images.githubusercontent.com/102492818/226956434-7454fd2b-f9fc-46ee-9fc7-611a54b9b314.mp4
</details>

---

<br />

Developed by [Marcelo Marques](https://www.linkedin.com/in/marcelo-mls/), © 2023.

<div>
  <a href = "https://www.linkedin.com/in/marcelo-mls/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" />
  </a>
  <a href="mailto:marcelo-mls@hotmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Hotmail-0077B5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>



