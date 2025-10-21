-- list all records of the table second_table not null or empty order by desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;