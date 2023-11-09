# 0x01. Basic Authentication

**1. What Authentication Means**

Authentication is the process of verifying the identity of a user, application, or system to grant access to a resource or service. It ensures that only authorized entities can perform certain actions or access specific data.

**2. What Base64 Is**

Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. It is commonly used for encoding binary data, such as images or files, into a format suitable for text-based protocols or storage.

**3. How to Encode a String in Base64**

Encoding a string in Base64 involves converting the characters in the string to their corresponding Base64 representation. Various programming languages and tools offer functions or libraries to perform this encoding. Typically, it results in a string composed of characters from the Base64 character set.

**4. What Basic Authentication Means**

Basic Authentication is a simple method of authentication used in HTTP-based communication. It involves sending a username and password in an HTTP request's Authorization header. The credentials are typically Base64-encoded and sent over the network.

**5. How to Send the Authorization Header**

Sending the Authorization header in an HTTP request involves including the credentials (username and password) as a Base64-encoded string in the header. The header is constructed as follows:
```shell
Authorization: Basic base64EncodedCredentials
```
Replace base64EncodedCredentials with the Base64-encoded string of your username and password separated by a colon (e.g., "username:password"). This header is commonly used for HTTP Basic Authentication.

## Core Components

### `SimpleAPI/`

A preliminary HTTP API code-base and configuration repository designed for future enhancements.

### `models/`

- `base.py`: Contains essential methods for object management and manipulation.
- `user.py`: Inherits core functionalities from `models/base.py` and adds methods for managing user attributes.

### `api/v1`

- `app.py`: Houses the application server's source code and serves as the entry point.
- `views/index.py`: Defines route endpoints for handling authentication status and data statistics.
- `views/users.py`: Manages CRUD functionalities for user objects within the application.

**`requirements.txt`**: Lists essential dependencies and their versions to ensure a consistent environment for the 
project.

## Project Setup

1. Create and activate a virtual environment for project development:
    ```shell
    $ python3 -m venv .virtual_environment_name_env
    $ source .virtual_environment_name_env/bin/activate
    ```
   - This step sets up an isolated environment for your project to manage dependencies.

2. Upgrade Python's package manager (pip) to the latest version available:
    ```shell
    $ pip3 install --upgrade pip
    ```
   - Ensures you have the most up-to-date package manager for dependency management.

3. Install the initial package dependencies necessary for development:
    ```shell
    $ pip3 install -r requirements.txt
    ```
   - Installs the required project dependencies listed in the `requirements.txt` file.

4. Start the application's server:
    ```shell
    $ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```
   - Launches the server to run your API application.

5. Test the API authentication endpoint in another terminal while the server is running:
    ```shell
    $ curl "http://0.0.0.0:5000/api/v1/status" -vvv
    ```
   - Verifies the functionality of the authentication endpoint by sending a request using the `curl` command.

## Author
Emeka Emodi
