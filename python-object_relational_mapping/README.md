# Python Object Relational Mapping (ORM)

## Overview

This directory contains exercises focused on **Object Relational Mapping (ORM) in Python** from the Holberton School Higher Level Programming track.

The exercises teach how to interact with MySQL databases using Python classes, mapping database tables to Python objects, and performing CRUD operations safely and efficiently.

---

## Learning Focus

This module demonstrates:

* Connecting Python to MySQL databases
* Creating Python classes to represent database tables (`State`, `City`)
* Performing CRUD operations using ORM concepts
* Executing parameterized SQL queries to prevent SQL injection
* Fetching, filtering, and manipulating database records through Python objects
* Mapping database relationships (e.g., cities to states)
* Understanding how Python objects can represent relational data

---

## Files and Tasks

| File                               | Purpose                                  |
| ---------------------------------- | ---------------------------------------- |
| `0-select_states.py`               | Query all states from the database       |
| `0-select_states.sql`              | SQL database setup for exercise          |
| `1-filter_states.py`               | Filter states by name using SQL queries  |
| `2-my_filter_states.py`            | Custom filtering using Python and SQL    |
| `3-my_safe_filter_states.py`       | Parameterized queries for safe filtering |
| `4-cities_by_state.py`             | List all cities grouped by state         |
| `4-cities_by_state.sql`            | SQL database setup for cities by state   |
| `5-filter_cities.py`               | List cities of a given state             |
| `6-model_state.py`                 | Define `State` class for ORM             |
| `6-model_state.sql`                | SQL setup for `State` table              |
| `7-model_state_fetch_all.py`       | Fetch all state objects sorted by id     |
| `7-model_state_fetch_all.sql`      | Database setup for fetch all states      |
| `8-model_state_fetch_first.py`     | Fetch the first state object             |
| `9-model_state_filter_a.py`        | Fetch state objects containing 'a'       |
| `10-model_state_my_get.py`         | Get state object by id                   |
| `11-model_state_insert.py`         | Insert a new state object into database  |
| `12-model_state_update_id_2.py`    | Update state object with id=2            |
| `13-model_state_delete_a.py`       | Delete state objects containing 'a'      |
| `14-model_city_fetch_by_state.py`  | Fetch all cities for a given state       |
| `14-model_city_fetch_by_state.sql` | SQL setup for city fetch by state        |
| `model_city.py`                    | Define `City` class for ORM              |
| `model_state.py`                   | Define `State` class for ORM             |
| `README.md`                        | Overview of ORM exercises                |

---

## Example Snippet

Example of defining a Python class for a database table using ORM concepts:

```python
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# Usage
new_state = State(name='California')
session.add(new_state)
session.commit()
```

This demonstrates mapping a table to a Python class and inserting a record.

---


## Skills Demonstrated

* Connecting Python applications to MySQL databases
* Mapping tables to Python classes
* Performing CRUD operations using Python objects
* Executing safe parameterized SQL queries
* Fetching and manipulating relational data via Python
* Understanding object-relational mapping principles

---

## Why This Matters

Mastering Python ORM is important because:

* It abstracts SQL operations into Python code, making development faster and safer
* Reduces risk of SQL injection through parameterized queries
* Allows developers to work with objects instead of raw SQL
* Forms the foundation for building data-driven Python applications with clean, maintainable code
