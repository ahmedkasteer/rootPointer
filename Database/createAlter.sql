ALTER TABLE employees        			-- allows us to alter table
MODIFY COLUMN email VARCHAR(100);			-- allows us to modify email col and datatype


ALTER TABLE employees 						-- we can move around email column using 
MODIFY email VARCHAR(100)
AFTER last_name;							-- after last name column. 

ALTER TABLE employees						-- we can also drop column using ALTER and then 
DROP COLUMN email;								-- DROP COLUMN email
SELECT * FROM employees;

ALTER TABLE employees
ADD COLUMN phone_num VARCHAR(15);			-- we can add new column table 

CREATE TABLE employees (				-- we can create new table using this command of CREATE TABLE
	employee_id INT,						-- followed by variable and its datatype
    first_name VARCHAR(50),					-- string (50) characters length. 
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5, 2),
    hire_date DATE
);

