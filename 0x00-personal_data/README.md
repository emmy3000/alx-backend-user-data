# 0x00. Personal data

## Overview
This project provides examples and implementations for handling Personally Identifiable Information (PII), log filtering, password encryption, and database authentication using environment variables.

## Personally Identifiable Information (PII)
Personally Identifiable Information (PII) refers to any information that can be used to identify an individual. PII includes data such as names, email addresses, phone numbers, social security numbers, and passwords. Protecting PII is essential to maintain data privacy and security.

## Log Filtering for PII
To ensure that PII remains secure in log files, the project demonstrates how to implement a log filter that obfuscates PII fields. This is achieved by redacting sensitive information in log messages using a custom formatter.

## Password Encryption and Validation
The project showcases how to hash and salt passwords using the bcrypt algorithm, a strong and secure password hashing technique. It covers the encryption of user passwords and how to check the validity of an input password by comparing it to the hashed password.

## Database Authentication with Environment Variables
To authenticate with a database securely, the project provides guidance on using environment variables. Storing sensitive database credentials in environment variables helps protect this information from unauthorized access.

## Usage
The code examples in this project illustrate how to implement log filtering, password encryption, and database authentication. It is essential to follow best practices for securing PII and sensitive data in your applications.

## Dependencies
- Python 3.x
- bcrypt library
- MySQL database or CSV file (for database authentication).

## Installation
To run the code examples and use the functionalities provided in this project, ensure you have the required dependencies installed. You can install them using package managers like pip.

For example, to install the bcrypt library, you can use the following command:

```shell
pip install bcrypt
```

## Running the Examples
Execute the provided Python scripts to see the examples in action. You can run the scripts using the following command:

```shell
python3 main.py
```
Make sure you follow best practices for securing PII and sensitive data in your own projects by applying the concepts demonstrated in this project.
