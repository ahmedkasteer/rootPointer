-- subqueries 
select *
from employee_demographics
where employee_id IN 
			(SELECT  employee_id
			 FROM employee_salary
			 WHERE dept_id = 1
			);

select first_name, salary,
(select avg(salary)
from employee_salary) as AVGSAL
from employee_salary;

select gender, avg(age), max(age), min(age), count(age) 
from employee_demographics
group by gender;	

select avg('max(age)') 
from 
(select gender, avg(age), max(age), min(age), count(age) 
from employee_demographics
group by gender) as agg_table



 