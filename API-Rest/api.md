# API Rest - What is it?

## API - Application Programming Interface

- I send a request and wait for a response
- APIs communicate with each other by different means: they can return anything data to status
- We develop now functionalities
- Easier to integrate, hence, easier to change between APIs
- Better performance

## API Types

- Public: we can acces its endpoint without any authentication
- Private: usually works in private systems, such as entrerprise systems
- Third party: its usually marketed and offered as a license to use the service

## Communication using API

- Usually made with `.xml` or `.json`. Simplier file types to use
- Requests are made through HTTP

## HTTP verbs

- GET: get a item
- POST: send an item
- DELETE: delete an item from the database
- PUT: update an item
- PATCH: update partially an item

## What is an endpoint?

- It's an API url tha we access to get a response
- Uses the API's domain or just another
- Those techniques are useful to reduce project's complexity and apply the REST standard

## What is a REST API

- Architecture conventions related to APIs and HTTP protocol
- It's basically a standard to make high quality APIs
- Those are the characteristics that a RESTful API has: 
    - Uniformity: the same endpoint must return the same items to different requests
    - Decoupling: the API should be independent from the front-end application
    - Stateless: the requests are unique and independent and saves must be done by the side which made the request
    - Cache: use of cache system to improve the access speed
    - Layered Architecture: code hierarchy must be followed
    - Code on demand: some code must be runned on demand

# Creating our first API using Python and Flask

## Setting things up in a Linux OS

First, since we are using python, we just need to install it and its package installer.

```bash
sudo apt install python3
sudo apt install pip3
```

### Creating a virtual environment

After the installation, let's create a virtual environment. This environment is useful to avoid incompatibility between other projects you may have in your operational system. It basically freezes and keeps the current state of the dependencies you are using. Hence, the packages you installed in a project will keep only on that project. With that explained, let's start creating it.

Create a new folder where your project will be placed

```bash
mkdir api && cd api
```

Let's create a `.venv` folder where your virtual environment will be placed

```bash
python3 -m venv .venv
```

Now a `.venv` folder was created in your project's directory. To check the recently created folder, use the command:

```bash
ls -lha
```

Since the directory was created, let's activate your brand new virtual environment

```bash
. .venv/bin/activate
```

Now that you are inside an environment we just need to install Flask using the package installer `pip` you previously downloaded

```bash
pip3 install Flask
```

And with Flask installed, we can list its dependencies and save it in a file

```bash
pip3 freeze > requirements.txt
```

You should see a list similar to this one in your `requirements.txt` file

```txt
blinker==1.8.2
click==8.1.7
Flask==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
Werkzeug==3.0.3
```

## Running a Flask Application

In order to run your API we need first create a python file. How you name it doesn't matter, but you need to pay attention to not name it `flask.py` because it would generate a conflict with Flask itself

```bash
touch hello.py
```

At your python file, you should write the code below

```python
from flask import Flask

app = Flask(__name__)

# http://localhost:5000/
@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"
```

This is how a minimal Flask application looks like. Basically we did:

1. Import a `Flask` class. An instance of this class will be our Web Server Gateway Interface (WSGI) Application
    - A WSGI is a mediatior between a web server and a Python web application, handling their communication
1. The `__name__` passed as an argument defines the name of the app's module or package in order to let Flask know where look for resources. This is a convenient shortcut for this and it's appropriete for most cases.
1. The `route()` method is used to tell Flask what URL should trigger the function
1. The function returns the message we want to display in the user's browser. The default content type is HTML, so, when written in a string, it will be rendered by the browser

In order to run you application, just type this command at the terminal

```bash
flask --app hello run
```

> [!Note]
> You can ommit the `--app` option if your file is named `app.py` or `wsgi.py`.
> In this case your commando would be just `flask run`

### Running the Debug mode

Simply run your application with the command

```bash
flask --app hello run --debug

# If you named your file app.py
flask run --debug
```
