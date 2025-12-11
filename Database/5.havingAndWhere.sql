-- having vs where
select gender, avg(age)
from employee_demographics
where avg(age) > 40
group by gender; -- gives error
-- having clause is designed for group by function. it performs functions on the groups whereas where function performs on individual rows. 
select gender, avg(age)
from employee_demographics
group by gender
having avg(age) > 40;

select * 
from employee_salary;

select occupation, avg(salary) 
from employee_salary
where occupation like '%manager%' -- works on row level and it returns occupation with "manager" mentioned in it. 
group by occupation
having avg(salary) > 75000 -- applied on groups of columns made by group by. 
