# Simple Python Website Project

## General
This is a [Simple Python Website Project](https://github.com/darumor/simple-python-website) that can be used for prototyping modern web services. 
This application is not very scalable nor data secure and thus should not be used in production.

The project uses 
- **ngrok** as a way to publish the service (no actual dependency) (https://ngrok.com/)
- **bottle** as web server / adapter (http://bottlepy.org/docs/dev/)
- **sqlite3** as database (https://www.sqlite.org/index.html)
- **SQLitePlugin** as database access method
- **vue.js 3** as frontend component framework (https://vuejs.org/)
- **vue router 4** as SPA router (https://router.vuejs.org/guide/)
- **bootstrap 5** as frontend styling system (https://getbootstrap.com/)
- **axios** as http client (https://axios-http.com/)
- **MD5** as password hashing method
- **Signed cookies** and credentials stored in the database for authentication 
- **Environment variables** for configuration


## Requirements
Install dependencies
    
    $ cd simple-python-website
    $ python3 -m venv venv/
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt

Update dependencies (if you make changes)
    
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
- Set http port for the service (SPW_PORT)
- Set session length / cookie TTL (SPW_SESSION_TTL)

Note: If environment variables are set, they override any / all default values

## Running the application
Terminal 1

    $ ngrok http 9999

Terminal 2

    $ python3 main.py

Browser1

    http://localhost:9999

Browser2

    http://some-random-url.ngrok.io

## Defaults
### Default admin credentials
Default password should be changed before publishing
 
    admin / admin-password

## Todo
There are still thing to do:
- separate authdata from users - table
- remove admin-account from migrations
- add admin-account to testdata and proddata
- two main.py's one for testing / developing and one for production, data-imports accordingly
- maybe separate different services to different db's to simulate microservices
- userroles and permissions in the cookie?
  - maybe use a local session storage for the access token
  - wrap axios into a wrapper that reads the local session storage