SELECT column1,
       CASE 
           WHEN condition1 THEN result1
           WHEN condition2 THEN result2
           ...
           ELSE resultN
       END AS new_column_name
FROM table_name;
