# Project README

This project is focused on setting up and deploying various versions of the AirBnB clone application on web servers using Python, Flask, Gunicorn, and Nginx. Below are the instructions for each task:

## Task 1: Set up development with Python

### Requirements:
- Ensure that task #3 of your SSH project is completed for web-01.
- Install the net-tools package on your server: `sudo apt install -y net-tools`
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app`.

## Task 2: Set up production with Gunicorn

### Requirements:
- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called `app`.
- Serve the same content from the same route as in the previous task using Gunicorn on port 5000.

## Task 3: Serve a page with Nginx

### Requirements:
- Nginx must serve the page from the route `/airbnb-onepage/` both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.

## Task 4: Add a route with query parameters

### Requirements:
- Nginx must serve the page from the route `/airbnb-dynamic/number_odd_or_even/(any integer)` both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5001.

## Task 5: Serve your AirBnB clone

### Requirements:
- Set up your Gunicorn instance to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Setup Nginx to route requests to your Gunicorn instance.
- Configure Nginx to properly serve the static assets found in `web_dynamic/static/`.

For detailed examples and configurations, please refer to the respective tasks and provided examples in the project repository.

Repo: [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
Directory: 0x1A-application_server
