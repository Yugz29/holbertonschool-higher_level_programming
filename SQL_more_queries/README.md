# SQL More Queries

## Overview

This directory contains intermediate SQL exercises from the **Higher Level Programming** track of the Holberton School curriculum.

The focus is on performing **advanced queries** that involve multiple tables, joins, aggregation, subqueries, and filtering. This builds on introductory SQL knowledge and prepares for complex data retrieval in real-world applications.

---

## Learning Focus

This module demonstrates:

* Writing queries involving multiple tables
* Using `JOIN` clauses (`INNER JOIN`, `LEFT JOIN`, etc.)
* Aggregation with `GROUP BY` and functions like `COUNT`, `SUM`, `AVG`
* Filtering grouped results using `HAVING`
* Writing subqueries and nested queries
* Sorting and limiting results
* Combining complex conditions

---

## Typical Files and Tasks

| File / Script               | Purpose                                    |
| --------------------------- | ------------------------------------------ |
| `0-join_queries.sql`        | Demonstrate basic JOIN operations          |
| `1-aggregate_functions.sql` | Use aggregation functions (`COUNT`, `SUM`) |
| `2-group_by_having.sql`     | Group results and filter groups            |
| `3-subqueries.sql`          | Nested and subquery examples               |
| `4-multiple_tables.sql`     | Complex queries involving multiple tables  |
| `README.md`                 | Overview of intermediate SQL tasks         |

> File names may vary. Ensure each script contains comments explaining the query purpose.

---

## Example SQL Snippet

```sql
SELECT department.name, COUNT(employee.id) AS total_employees
FROM department
JOIN employee ON employee.department_id = department.id
GROUP BY department.name
ORDER BY total_employees DESC;
```

This query joins two tables, counts the number of employees per department, and sorts the result.

---

## Skills Demonstrated

* Combining data from multiple tables using JOINs
* Aggregating data to summarize information
* Filtering grouped results with `HAVING`
* Writing subqueries for nested logic
* Structuring complex queries clearly and efficiently

These skills are essential for working with relational databases in real-world applications.

---

## Why This Matters

Intermediate SQL knowledge is important because:

* Real applications often require querying multiple tables simultaneously
* Efficient queries improve application performance
* Understanding joins, aggregation, and subqueries is foundational for backend and data-focused roles
* Prepares for advanced database operations and analytics
