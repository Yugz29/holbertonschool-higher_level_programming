# Python Server-Side Rendering

## Overview

This directory contains exercises focused on **server-side rendering with Python** from the Holberton School Higher Level Programming track.

The exercises teach how to generate dynamic HTML content on the server using Python, templates, and various data sources such as JSON, CSV, and SQLite databases.

---

## Learning Focus

This module demonstrates:

* Creating dynamic HTML pages using templates
* Using Flask and Jinja2 for server-side rendering
* Looping and conditional logic within templates
* Reading and displaying data from JSON and CSV files
* Integrating SQLite databases for dynamic content
* Handling data and templates safely and efficiently

---

## Files and Tasks

| File               | Purpose                                                              |
| ------------------ | -------------------------------------------------------------------- |
| `templates/`       | Folder containing HTML templates with dynamic rendering using Jinja2 |
| `items.json`       | JSON data used in templates                                          |
| `products.csv`     | CSV data used in templates                                           |
| `products.json`    | Additional JSON data for rendering                                   |
| `products.db`      | SQLite database to extend dynamic content                            |
| `template.txt`     | Simple template example for practice                                 |
| `task_00_intro.py` | Introductory Python file for server-side rendering                   |
| `task_01_jinja.py` | Basic HTML template rendering with Flask                             |
| `task_02_logic.py` | Implement logic and conditions in templates                          |
| `task_03_files.py` | Display data from JSON or CSV files in templates                     |
| `task_04_db.py`    | Extend dynamic data to include SQLite database content               |

---

## Example Snippet

Example of rendering a template with Flask and Jinja2:

```python
from flask import Flask, render_template
import json

app = Flask(__name__)

with open('items.json') as f:
    items = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
```

In the template (`index.html`):

```html
<ul>
{% for item in items %}
    <li>{{ item.name }} - ${{ item.price }}</li>
{% endfor %}
</ul>
```

This demonstrates dynamically generating HTML content based on JSON data.

---

## Skills Demonstrated

* Server-side rendering with Flask and Python
* Using Jinja2 templates for dynamic HTML
* Reading and displaying JSON and CSV data
* Integrating SQLite databases for dynamic content
* Looping and conditional rendering in templates
* Writing maintainable and modular Python web applications

---

## Why This Matters

Mastering server-side rendering in Python is important because:

* It allows building dynamic, data-driven web pages
* Templates separate logic from presentation for cleaner code
* Understanding server-side rendering is foundational for web development
* Skills are transferable to Flask, Django, and other Python web frameworks
