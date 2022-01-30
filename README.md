
# Blog Site  

Web Blog using Python/Django.

You can visit the site by following this [link.](http://3.142.247.127/)

## Overview

This is my first web project. It's full-featured web-application, where people can create a profile, write posts, leave comments, reset their password and so on.
I've learned a lot of things along the way, such as how to create an API, deploy a project or build interfaces using Bootstrap. I faced some challenges and it made me
learn new things and look for better solutions.

## Technologies Used

- HTML5
- CSS3
- Bootstrap
- Python
- Django
- Django Rest Framework
- Git
- GitHub
- Docker
- Docker Compose
- uWSGI
- Nginx
- AWS EC2

## Deployment

To deploy the project follow these steps.

1. Clone the project:

```Shell
git clone https://github.com/AndrejTsvetkov/my_website.git
```

2. Install Git on your deployment server.

3. Install Docker and Docker Compose (for the latter you can use the following [link](https://docs.docker.com/compose/install/)).

4. Create .env file and specify your own environment variables (you can see an example of how to set variables in the [.env.sample](./.env.sample) file)

5. Create a directory `./media`. It has to be in the root directory of your project.

6. Put in the `./media` directory an image you would like to use as the default profile picture for all new users.
The image must be named `default.jpg`.

7. Create superuser you will use to log in to the admin page:

```Shell
docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"
```

8. Build the images and run the containers:

```Shell
docker-compose -f docker-compose-deploy.yml up -d --build
```

9. Test it out at ip-adress and port you specified in .env and [docker-compose-deploy.yml](./docker-compose-deploy.yml) files.
Make sure that you have the port opened on your deployment machine. Also if you change the proxy port inside your container you should change the [default.conf](./proxy/default.conf) file as well.

## Sending email

The functionality of the site allows users to reset their passwords as needed by sending a reset password email to themselves that then links to a change password form.

Sending email can be implemented in various ways (for example you can use  AWS SES service), but for testing purposes i chose the simple way by using a google account, but
it can be a little tricky, so if you want to get a full-featured web application you should follow these steps.

1. Create a google account you will be using for sending emails.

2. Visit your google account [security page](https://myaccount.google.com/security).

3. Turn on two-step authentication. 

4. On the security page click the tab for App passwords.

5. Generate password, you can enter a descriptive name for the application you want to authorize, such as "Django gmail".

6. Write down the password.

7. In the section above we said that to successfully deploy the project you need to specify your own environment variables. 
Some of these variables are `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`, so you are to set your email as the first one and the generated password as the second.

You may be wondering why i don't simple use the password of my email in the `EMAIL_HOST_PASSWORD` variable. The reason is because Google cares about the security
of your account and will block attempts to authorize from insecure apps.

## Roadmap

- [ ] Enable HTTPS with a free SSL/TLS Certificate

- [ ] Use a custom domain name

- [ ] Use AWS S3 for file uploads

- [x] Add a comments section

- [ ] Add comment updates without reloading the page (use Django Channels)

- [x] Add a sidebar with the most popular posts

- [x] Add containerization using Docker and Docker Compose

## Authors

- [@AndrejTsvetkov](https://www.github.com/AndrejTsvetkov)
