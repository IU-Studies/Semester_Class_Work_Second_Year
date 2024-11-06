/* Left Outer Join */
SELECT columns
FROM table1
LEFT OUTER JOIN table2
ON table1.common_column = table2.common_column;

/* Right Outer Join */
SELECT columns
FROM table1
RIGHT OUTER JOIN table2
ON table1.common_column = table2.common_column;

/* Full Outer Join */
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.common_column = table2.common_column;
