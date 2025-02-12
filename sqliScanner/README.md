# SQL Injection Vulnerability Scanner

This project is a simple Python-based tool designed to scan a website for SQL injection vulnerabilities. It works by analyzing all forms on a given URL, submitting them with malicious inputs, and checking the response for signs of SQL injection errors.

## Prerequisites

Before running the tool, ensure that you have the following dependencies installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using `pip`:

pip install requests beautifulsoup4

## How It Works

The script performs the following steps:

1. **Finds all forms**: It retrieves all the forms present on a web page using the `BeautifulSoup` library.
2. **Gathers form details**: For each form, the script gathers details such as the form action URL, method (`GET` or `POST`), and the input fields.
3. **Injects test payloads**: The script injects test payloads like `"`, `'`, or other characters into the input fields of the form.
4. **Submits forms**: The script submits the form data, either via `GET` or `POST` method, to the server.
5. **Checks for vulnerabilities**: The script checks the server's response for SQL error messages that suggest an SQL injection vulnerability.

## Features

- **Scan for SQL injection vulnerabilities**: Detects common SQL injection errors in web forms.
- **Supports GET and POST requests**: Handles both types of form submissions.
- **Malicious payload injection**: Uses basic test inputs (`"`, `'`) to trigger potential SQL errors.
- **Detailed output**: Provides feedback for each form on whether a SQL injection vulnerability was detected.

## Functions

- `get_forms(url)`: Retrieves all forms present on a given URL.
- `form_details(form)`: Extracts the action, method, and input fields from the form.
- `vulnerable(response)`: Checks the response for SQL error messages indicating vulnerability.
- `sql_injection_scan(url)`: Scans a website for SQL injection vulnerabilities by analyzing all forms.
