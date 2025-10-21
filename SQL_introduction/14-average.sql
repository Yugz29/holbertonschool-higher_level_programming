-- compute the score average of all records in the table second_table
SELECT CONCAT('average', CHAR(10), AVG(score)) FROM second_table;