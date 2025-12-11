-- limit and aliasing 
select * from employee_demographics;
select * 
from employee_demographics
limit 3; -- specifies how many rows we want in our output returns top 3 rows from our table. 
-- if we want three oldest employees combine order by and limit together to get powerful results. 
select first_name, last_name, age, gender from employee_demographics
order by age desc limit 3; 

-- we can also use:
select first_name, last_name, age, gender from employee_demographics
order by age desc limit 2, 1; -- where 2 means start position and 1 means the first row after start position we want
-- so we have for e.g:
-- name 	age 	
-- jerry 	61
-- donna	46
-- leslie 	44 
-- limit 2,1 returns leslie age 44 because we started from second pos.(donna) and returned 1 after it. 

-- aliasing:- just change name of columns. 
select gender sex, avg(age) as avg_age -- whatever followed by as shows in output we may or may not use as. like gender sex.
from employee_demographics
group by gender
having avg_age > 40;
