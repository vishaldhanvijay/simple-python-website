# Simple python website project

## Requirements

### Install Ngrok
First register an Ngrok account and verify your email

$ snap install ngrok
$ ngrok authtoken .... 


## Configuration
- Set cookie secret
- Set database file
- Set password hash key


## Running the application

Terminal 1
$ ngrok http 9999

Terminal 2
$ python3 hello.py

Browser1
http://localhost:9999/hello/NAME

Browser2
http://some-random-url.ngrok.io/hello/NAME
