SQL Scratchpad Project (PopSQL)
 Overview
This project contains SQL queries written and tested using PopSQL, a collaborative SQL editor.
It demonstrates fundamental SQL concepts using a student table, including filtering, conditions, and result limiting.
________________________________________
Database Structure
Table: student
Column Name	Data Type	Description
student_id	INT	Unique identifier for each student
name	VARCHAR	Name of the student
major	VARCHAR	Field of study (e.g., Politics, Comp Sci, History)
________________________________________
 SQL Concepts Covered
This project practices the following SQL concepts:
•	SELECT statements
•	WHERE filtering
•	IN operator
•	Comparison operators (=, <>, >, <)
•	Logical operators (AND, OR)
•	LIMIT clause
•	SQL comments (--, /* */)
•	Query structure rules
________________________________________
 Example Queries
1. Select all students
SELECT * FROM student;
________________________________________
2. Filter using IN
SELECT *
FROM student
WHERE major IN ('Politics', 'Comp Sci', 'History');
________________________________________
3. Filter using multiple conditions
SELECT *
FROM student
WHERE student_id > 3
AND name <> 'Jack';
________________________________________
4. Limit results
SELECT *
FROM student
WHERE major IN ('Politics', 'Comp Sci', 'History')
LIMIT 2;
________________________________________
5. Using comments
SELECT *
FROM student
-- WHERE student_id > 3
-- AND name <> 'Jack';
________________________________________
 Common Mistakes to Avoid
•	❌ Using AND LIMIT (invalid syntax)
•	❌ Writing comments incorrectly like --WHERE
•	❌ Forgetting IN requires parentheses
•	❌ Confusing LIMIT with a condition
•	❌ Incorrect query order
________________________________________
SQL Query Structure
Standard SQL order:
SELECT columns
FROM table
WHERE conditions
GROUP BY columns
HAVING conditions
ORDER BY columns
LIMIT number;
________________________________________
Key Takeaways
•	IN = match any value in a list

•	<> = not equal

•	-- = single-line comment

•	LIMIT = restrict number of results

•	SQL must follow strict syntax rules
________________________________________
Tools Used
•	PopSQL (SQL editor)
•	MySQL syntax
________________________________________
 Author
It is a Practical approach for beginner to learn SQL fundamentals.
