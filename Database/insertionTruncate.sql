INSERT INTO employees													-- we use INSERT INTO tablename VALUES (),(); to insert values row wise. 
VALUES (1, "Eugene", "Krabs", "25.50", "2023-01-02","+923127999248"),
       (2, "Squidward", "Tentacles", "15.00", "2023-01-03","+923127999244"),
       (3, "Spongebob", "Squarepants", "12.50", "2023-01-04","+923127999284"),
       (4, "Patrick", "Star", "12.50", "2023-01-05","+923127999700"),	 
	   (5, "Sandy", "Cheeks", "17.25", "2023-01-06","+923127999800");	-- inserting vals according to data type
-- if we try to add (6,"Sheldon", "Plankton", "16.20") will give error since missing values of date and phone number. 
-- the fix is this:
INSERT INTO employees (emplyee_id, first_name, last_name) -- explicitly mention name of columns. 
VALUES (6, "Sheldon", "Plankton");  -- rest of columns will be NULL. 


SELECT * FROM employees; 												-- display entire table. 

TRUNCATE TABLE employees;						-- for removal of data keeping all rows and columns only all data is removed. 


