-- Unions -- allows union on different tables and columns of same data type returns unique values from both table. 
-- union by default uses distinct 
-- if we want all union data we use "UNION ALL"
select first_name, last_name
from employee_demographics
union
select first_name, last_name
from employee_salary;
-- ^^ this returns unique names from both tables. 
select first_name, last_name
from employee_demographics
union all
select first_name, last_name 
from employee_salary;
-- ^^ this gives us all the values from A-Z with same column name 

select first_name, last_name, 'Old Man' as Label
from employee_demographics
where age > 40 AND gender = 'Male'
UNION
select first_name, last_name, 'Old Lady' as Label
from employee_demographics
where age > 40 AND gender = 'Female'
UNION
select first_name, last_name, 'Highly Paid Employee' as Label
from employee_salary
where salary > 70000
order by first_name, last_name;

-- ^^ this gives us example of how we can use multiple unions and then use them together to select multiple data 


