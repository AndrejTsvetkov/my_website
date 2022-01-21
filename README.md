
# Blog Site  

This is my first web project. It's a blog where people can read, add, delete and update posts.

## Demo

You can visit the site by following this [link.](http://3.142.247.127/)

## Deployment

To deploy the project follow these steps.

1. Clone the project:

```Shell
git clone https://github.com/AndrejTsvetkov/my_website.git
```

2. Install Git on your deployment server.

3. Install Docker and Docker Compose (for the latter you can use the following [link.](https://docs.docker.com/compose/install/)

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
## Roadmap

- [ ] Enable HTTPS with a free SSL/TLS Certificate

- [ ] Use a custom domain name

- [ ] Use AWS S3 for file uploads

- [x] Add a comments section

- [ ] Add comment updates without reloading the page (use Django Channels)

- [x] Add containerization using Docker and Docker Compose

## Authors

- [@AndrejTsvetkov](https://www.github.com/AndrejTsvetkov)
