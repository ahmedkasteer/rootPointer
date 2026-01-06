select first_name, last_name, age,
-- we use case stamements to get multiple cases for age 
case 
	when age <= 30 then 'Young'
    when age between 31 and 50 then 'Old'
    when age >= 50 then "On Death's Door"
end as age_bracket
-- to label the case stament column, we use as after end ^^ 
from employee_demographics;

-- we need to get pay increase and bonus 
-- < 50000 = 5% raise
-- < 70000 = 7% raise
-- if in finance = 10% bonus
select first_name, last_name, salary, 
case 
	when salary < 50000 then salary + (salary* 0.05)
    when salary > 50000 then salary + (salary * 0.07)
end as new_Salary,
case 
	when dept_id = 6 then salary * 0.10
end as bonus
from employee_salary;
-- ^^ this gives us cases where we can apply queries to update salary and return new salary according to the constraints. 

select *
from employee_salary;
select *
from parks_departments;

