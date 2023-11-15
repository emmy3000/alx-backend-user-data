# 0x03. User authentication service

## Overview

This documentation outlines the implementation and understanding of a basic user authentication service in the 
context of a Flask web application. While it's emphasized in industry to use established modules or frameworks for 
authentication (such as `Flask-User` in the case of Python-Flask), this project serves as a learning exercise to 
comprehend the underlying mechanisms by building from scratch.

## Key Learning Objectives

In this section, simple and basic implementations are utilized in enabling the application server carry out 
essential tasks necessary for establishing robust user authentication services.

1. **Declaring API Routes in a Flask App:**

In this section, we delve into the process of declaring API routes within a Flask application. Understanding how to 
structure and define routes is fundamental to creating an effective authentication service. 

Example:

```python

from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Implementation for user login
    pass

@app.route('/logout', methods=['GET'])
def logout():
    # Implementation for user logout
    pass
```

2. **Getting and Setting Cookies:**

Cookies play a crucial role in web authentication. Learn how to handle cookies to maintain user sessions and store 
relevant information securely. 

Example:

```python

from flask import request, make_response

@app.route('/login', methods=['POST'])
def login():
    # User authentication logic
    user_id = authenticate_user(request.form['username'], request.form['password'])

    if user_id:
        # Set a cookie to maintain the user session
        response = make_response("Login successful")
        response.set_cookie('user_id', str(user_id))
        return response
    else:
        return "Login failed"
```

3. **Retrieving Request Form Data:**

Understanding how to retrieve and process data from incoming requests is essential for user authentication. In 
Flask, this often involves accessing form data submitted through HTTP POST requests.

Example:

```python

from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # User authentication logic
    # ...
```

4. **Returning Various HTTP Status Codes:**

Effectively communicating the status of operations is critical. Learn how to return appropriate HTTP status codes 
to indicate success, failure, or other relevant conditions.

Example:

```python

from flask import abort

@app.route('/login', methods=['POST'])
def login():
    if authentication_successful:
        return "Login successful", 200
    else:
        abort(401, "Authentication failed")
```

## Project Setup

Setting up the project involves creating a structured environment and managing dependencies to ensure a seamless 
development process.

**NOTE:** *The following steps for setting up a project must be undertaken before carrying out other implementations, 
including all code logic definitions found under the sub-header "Key Learning Objectives".*

1. **Project Repository:**

Create a new directory to serve as the project's code base and navigate into it:

```shell
$ mkdir 0x03-user_authentication_service
$ cd 0x03-user_authentication_service
```

2. **Virtual Environment:**

Create and activate a virtual environment for project isolation and dependency management:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

3. **Package Management Upgrade:**

Ensure Python's package manager (`pip`) is up to date within the virtual environment:

```shell
(.venv)$ pip install --upgrade pip
```

4. **Installation of Package Dependencies:**

This project is an extension of a previous project located in the directory `"0x02-Session_authentication/"`. To 
maintain consistency, install the dependencies used in that project into the current one:

```shell
(.venv)$ pip3 install -r ../0x02-Session_authentication/requirements.txt
```

5. **Introducing New Package Dependencies:**

`Bcrypt` *Module:*

The `Bcrypt` module provides a secure method for hashing passwords using the bcrypt hashing algorithm. This 
algorithm is deliberately slow and computationally intensive, enhancing resistance to brute-force attacks.

```shell
(.venv)$ pip3 install bcrypt
```

`SQLAlchemy` *Module:*

It's a robust SQL toolkit and Object-Relational Mapping (ORM) library for Python. It simplifies database access and 
manipulation by allowing developers to use Python objects and methods instead of raw SQL queries.

```shell
(.venv)$ pip3 install SQLAlchemy
```

6. **Project's Personal Package Dependencies:**

In step 4, dependencies from a previous project were introduced, and in step 5, new dependencies specific to this 
project (`bcrypt` and `SQLAlchemy`) were added. To manage these dependencies efficiently, create and populate a 
`requirements.txt` file:

```shell
(.venv)$ pip3 freeze > requirements.txt
```

By following these steps, a clean and organized environment will be established for developing the user 
authentication service.

## Conclusion

In summary, this documentation serves as a guide for building a simple and basic user authentication service in Flask.
It focuses on key objectives such as defining *API routes*, *handling cookies*, *processing form data*, and 
*managing HTTP status codes*.

The project setup section ensures a smooth start, covering repository creation, virtual environment setup, and 
package installations. By following these steps, you're well-prepared to commence development on a clean and 
organized user authentication service project. Happy coding!

## Author 
Emeka Emodi