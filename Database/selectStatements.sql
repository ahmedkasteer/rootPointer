SELECT first_name, last_name 				-- in order to get only speicifc columns. 
FROM employees;

SELECT * 
FROM employees
WHERE emplyee_id = 1;						-- gives specific return with a special condition. using 
											-- WHERE clause. 
-- or 
SELECT phone_num -- or * to get all data							-- to get phone number of specific user. 
FROM employees
WHERE first_name = "Spongebob";
-- or to get certain people with salary higher than a given amount. 
SELECT *
FROM employees
WHERE hourly_pay >= 15.00;
-- or 
SELECT *
from employees
where hire_date <= "2023-01-03" ;  				-- where employees hired before given date. 
-- or 
select * 
from employees
where emplyee_id != 1; 				-- not comparison operator. 
-- need to change column name wait a moment. 
alter table employees
rename column emplyee_id to employee_id;
-- ok gucci. 
select * 
from employees
where hire_Date IS NULL;					-- will return specific column having NULL attribute. 

select * 
from employees
where hire_Date IS NOT NULL;				-- will return specific columns not having NULL attributes 



