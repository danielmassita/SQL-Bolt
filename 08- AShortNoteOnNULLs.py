# https://sqlbolt.com/lesson/select_queries_with_nulls

"""
As promised in the last lesson, we are going to quickly talk about NULL values in an SQL database. It's always good to reduce the possibility of NULL values in databases because they require special attention when constructing queries, constraints (certain functions behave differently with null values) and when processing the results.

An alternative to NULL values in your database is to have data-type appropriate default values, like 0 for numerical data, empty strings for text data, etc. But if your database needs to store incomplete data, then NULL values can be appropriate if the default values will skew later analysis (for example, when taking averages of numerical data).

Sometimes, it's also not possible to avoid NULL values, as we saw in the last lesson when outer-joining two tables with asymmetric data. In these cases, you can test a column for NULL values in a WHERE clause by using either the IS NULL or IS NOT NULL constraint.
"""
# Select query with constraints on NULL values
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
"""
Exercise
This exercise will be a sort of review of the last few lessons. We're using the same Employees and Buildings table from the last lesson, but we've hired a few more people, who haven't yet been assigned a building.

Table: Buildings (Read-Only)
Building_name	Capacity
1e	24
1w	32
2e	16
2w	20

Table: Employees (Read-Only)
Role	Name	Building	Years_employed
Engineer	Becky A.	1e	4
Engineer	Dan B.	1e	2
Engineer	Sharon F.	1e	6
Engineer	Dan M.	1e	4
Engineer	Malcom S.	1e	1
Artist	Tylar S.	2w	2
Artist	Sherman D.	2w	8
Artist	Jakob J.	2w	6
Artist	Lillia A.	2w	7
Artist	Brandon J.	2w	7
Manager	Scott K.	1e	9
Manager	Shirlee M.	1e	3
Manager	Daria O.	2w	6
Engineer	Yancy I.		0
Artist	Oliver P.		0

Exercise 8 — Tasks
Find the name and role of all employees who have not been assigned to a building
Find the names of the buildings that hold no employees
"""
SELECT Name, Role FROM Employees
WHERE Building IS NULL;

SELECT * FROM Buildings
LEFT JOIN Employees 
    ON Buildings.Building_name = Employees.Building;
# THEN 
SELECT * FROM Buildings
LEFT JOIN Employees 
    ON Buildings.Building_name = Employees.Building
WHERE Name IS NULL;
# Name, Role, etc. could be used...