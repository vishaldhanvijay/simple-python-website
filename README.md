# Simple Python Website Project

## General
This is a Simple Python Website Project that can be used for prototyping web services. 
This application is not very scalable nor data secure and thus should not be used in production.

The project uses 
- **ngrok** as a way to publish the service (no actual dependency) (https://ngrok.com/)
- **bottle** as web server / adapter (http://bottlepy.org/docs/dev/)
- **sqlite3** as database (https://www.sqlite.org/index.html)
- **vue.js** as frontend framework (https://vuejs.org/)
- **axios** as http client (https://axios-http.com/)
- **bootstrap 5** as style system (https://getbootstrap.com/)
- **MD5** as password hashing method
- **Signed cookies** and credentials stored in the database for authentication 
- **Environment variables** for configuration

## Requirements
Install dependencies
    
    $ cd simple-python-website
    $ python3 -m venv venv/
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt

Update dependencies
    
    $ cd simple-python-website
    $ source venv/bin/activate
    $ pip freeze > requirements.txt


### Install Ngrok
First register an Ngrok account and verify your email

    $ snap install ngrok
    $ ngrok authtoken .... 

## Configuration
Using environment variables (while developing edit data/config.py)
- Set database filename (SPW_DATABASE_FILENAME)
- Set migrations filename (SPW_MIGRATIONS_FILENAME)
- Set data directory path (SPW_DATA_DIRECTORY)
- Set static files directory path (SPW_STATIC_FILES_DIRECTORY)
- Set cookie secret (SPW_COOKIE_SECRET)
- Set password hash key (SPW_PASSWORD_SECRET)

Note: If environment variables are set, they override any / all default values

## Running the application
Terminal 1

    $ ngrok http 9999

Terminal 2

    $ python3 web/main.py

Browser1

    http://localhost:9999

Browser2

    http://some-random-url.ngrok.io

## Defaults
### Default admin credentials
Default password should be changed before publishing
 
    admin / admin-password
