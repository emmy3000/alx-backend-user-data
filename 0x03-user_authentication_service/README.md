# 0x03. User authentication service

## Overview

This documentation outlines the implementation and understanding of a basic user authentication service in the context of a Flask web application. While it's emphasized in industry to use established modules or frameworks for authentication (such as Flask-User in the case of Python-Flask), this project serves as a learning exercise to comprehend the underlying mechanisms by building from scratch.

## Key Learning Objectives
1. **Declaring API Routes in a Flask App:**

In this section, we delve into the process of declaring API routes within a Flask application. Understanding how to structure and define routes is fundamental to creating an effective authentication service.
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

Cookies play a crucial role in web authentication. Learn how to handle cookies to maintain user sessions and store relevant information securely.
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

Understanding how to retrieve and process data from incoming requests is essential for user authentication. In Flask, this often involves accessing form data submitted through HTTP POST requests.
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

Effectively communicating the status of operations is critical. Learn how to return appropriate HTTP status codes to indicate success, failure, or other relevant conditions.
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

## Author 
Emeka Emodi