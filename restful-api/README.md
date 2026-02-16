# RESTful API

## Overview

This directory contains exercises focused on **RESTful API development and interaction using Python** from the Holberton School Higher Level Programming track.

The exercises teach how to create, interact with, and secure APIs using Python, HTTP requests, and Flask.

---

## Learning Focus

This module demonstrates:

* Making HTTP requests and handling responses in Python
* Using `requests` library to interact with APIs
* Creating basic HTTP servers using Python
* Developing RESTful APIs with Flask
* Handling routes, methods, and URL parameters
* Implementing basic security measures for APIs

---

## Files and Tasks

| File                        | Purpose                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| `task_02_requests.py`       | Make HTTP requests, retrieve and save posts from an API            |
| `task_03_http_server.py`    | Create a basic HTTP server using Python's `http.server` module     |
| `task_04_flask.py`          | Develop a simple Flask application with routes and dynamic content |
| `task_05_basic_security.py` | Add basic authentication and security measures to a Flask API      |

---

## Example Snippet

Example of making a GET request and saving the response:

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    posts = response.json()
    with open('posts.json', 'w') as f:
        import json
        json.dump(posts, f)
```

Example of a basic Flask route:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, RESTful API!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Skills Demonstrated

* Making HTTP requests and handling responses
* Reading and saving JSON data from APIs
* Creating basic HTTP servers and RESTful APIs
* Using Flask to define routes and dynamic content
* Adding basic security/authentication to API endpoints
* Debugging and testing API functionality

---

## Why This Matters

Mastering RESTful API development and interaction in Python is important because:

* APIs are fundamental to modern web applications
* Enables programmatic data exchange between systems
* Understanding HTTP methods and routes is crucial for backend development
* Security awareness is key for protecting data and endpoints
* Forms the foundation for full-stack Python development
