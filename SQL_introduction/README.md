# SQL Introduction

## Overview

This directory contains introductory SQL tasks from the **Higher Level Programming** track of the Holberton School curriculum.

The goal is to learn how to work with **relational databases** using SQL — the standard language for managing and querying structured data. It covers creating tables, inserting and retrieving data, filtering results, and writing basic queries.

---

## Learning Focus

This module demonstrates:

* Creating and using databases and tables
* Writing basic `SELECT` statements
* Filtering results using `WHERE`
* Sorting and limiting query results
* Using simple functions to manipulate data
* Inserting new records
* Updating and deleting data
* Understanding SQL syntax and structure

---

## Typical Files and Tasks

| File / Script                | Purpose                            |
| ---------------------------- | ---------------------------------- |
| `0-create_database.sql`      | Creates a database and tables      |
| `1-select_basic.sql`         | Basic `SELECT` queries             |
| `2-filter_conditions.sql`    | Use `WHERE` to filter results      |
| `3-sort_limit.sql`           | Sort and limit output              |
| `4-insert_update_delete.sql` | Modify table data                  |
| `README.md`                  | Overview of SQL introduction tasks |

> File names may vary — ensure each script is documented with comments explaining its purpose.

---

## Example SQL Snippet

```sql
SELECT first_name, last_name
FROM employees
WHERE city = 'San Francisco'
ORDER BY last_name ASC;
```

This query selects the first and last names of employees living in San Francisco and sorts the results alphabetically by last name.

---

## How to Run SQL Files

Use a MySQL server (or any compatible SQL DBMS):

```sh
mysql -u root -p < 0-create_database.sql
mysql -u root -p database_name < 1-select_basic.sql
```

Replace `database_name` with the database created in the first script.

---

## Skills Demonstrated

This project highlights your ability to:

* Write fundamental SQL queries
* Understand core relational database concepts
* Manipulate and retrieve data effectively
* Structure queries for readability and correctness

This is a critical foundation for backend development and working with real-world applications that rely on database storage.

---

## Why This Matters

SQL is a core skill for developers because:

* Most backend systems depend on databases
* Data retrieval and manipulation are at the heart of web applications
* Writing efficient queries improves performance
* Understanding relational models is essential for backend logic

Mastering SQL fundamentals prepares you for more advanced data tasks (joins, aggregation, indexing, optimization).
