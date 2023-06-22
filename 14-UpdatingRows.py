# https://sqlbolt.com/lesson/updating_rows

"""
SQL Lesson 14: Updating rows
In addition to adding new data, a common task is to update existing data, which can be done using an UPDATE statement. Similar to the INSERT statement, you have to specify exactly which table, columns, and rows to update. In addition, the data you are updating has to match the data type of the columns in the table schema.
"""
# Update statement with values
UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;
"""
The statement works by taking multiple column/value pairs, and applying those changes to each and every row that satisfies the constraint in the WHERE clause.

Taking care
Most people working with SQL will make mistakes updating data at one point or another. Whether it's updating the wrong set of rows in a production database, or accidentally leaving out the WHERE clause (which causes the update to apply to all rows), you need to be extra careful when constructing UPDATE statements.

One helpful tip is to always write the constraint first and test it in a SELECT query to make sure you are updating the right rows, and only then writing the column/value pairs to update.

Exercise
It looks like some of the information in our Movies database might be incorrect, so go ahead and fix them through the exercises below.

Table: Movies
Id	Title	Director	Year	Length_minutes
1	Toy Story	John Lasseter	1995	81
2	A Bug's Life	El Directore	1998	95
3	Toy Story 2	John Lasseter	1899	93
4	Monsters, Inc.	Pete Docter	2001	92
5	Finding Nemo	Andrew Stanton	2003	107
6	The Incredibles	Brad Bird	2004	116
7	Cars	John Lasseter	2006	117
8	Ratatouille	Brad Bird	2007	115
9	WALL-E	Andrew Stanton	2008	104
10	Up	Pete Docter	2009	101
11	Toy Story 8	El Directore	2010	103
12	Cars 2	John Lasseter	2011	120
13	Brave	Brenda Chapman	2012	102
14	Monsters University	Dan Scanlon	2013	110

Exercise 14 — Tasks
The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
The year that Toy Story 2 was released is incorrect, it was actually released in 1999
Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
"""
SELECT * FROM movies;

SELECT Title, Director FROM Movies
WHERE Title = "A Bug's Life"
# Then...
UPDATE Movies
SET Director = 'John Lasseter' 
WHERE Id = '2';

SELECT Id, Title, Year FROM movies
WHERE Title LIKE "%toy story%";
# Then... Let's change BY ID! 
UPDATE Movies
SET Year = '1999' 
WHERE Id = '3';

SELECT Id, Title, Director FROM movies
WHERE Title LIKE "%toy story%";
# Then...

UPDATE Movies
SET Director = 'Lee Unkrich', Title = 'Toy Story 3'
WHERE Id = '11';
