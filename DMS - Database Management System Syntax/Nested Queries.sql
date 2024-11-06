/*Single-Row Subquery in WHERE Clause*/
SELECT column1, column2
FROM table_name
WHERE column1 = (SELECT column FROM other_table WHERE condition);

/*Multiple-Row Subquery with IN*/
SELECT column1, column2
FROM table_name
WHERE column1 IN (SELECT column FROM other_table WHERE condition);

/*Correlated Subquery*/
SELECT column1, column2
FROM table_name AS t1
WHERE column1 = (SELECT aggregate_function(column) FROM other_table AS t2 WHERE t1.column2 = t2.column3);
