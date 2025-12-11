-- group by 
select * 
from employee_demographics;

select gender 
from employee_demographics
group by gender;  -- if not performing aggregate functions (AVG,MIN,MAX,SUM) then select and group by should be same. i.e gender here. 

-- we are using aggregate function here calculating avg of both females and males age. 
select gender, avg(age)
from employee_demographics
group by gender;

select occupation, salary from employee_salary
group by occupation, salary; -- since we are using 2 columns to group by, individual values according to them are grouped by
-- so salary grouped by their values and occupation grouped by their values. 
-- office manager shows twice because of 2 different salaries i.e 50k and 60k. if salary was same it would return single office manager. 

select gender, avg(age), max(age), min(age), count(age) from employee_demographics
group by gender; -- gives us avg age and max age and min age and count of employees grouped together by gender. 

-- order by 
-- sorts result in ascending or descending order. 
select *
from employee_demographics
order by first_name ASC; -- asc / DESC based on our preference. 

select *
from employee_demographics
order by gender DESC, age ASC; -- gives us age in descending males first and ascending age younger to older. 

-- can also be done using 
select * from employee_demographics
order by 5, 4; -- using column positions 5th is gender and 4th is age. 

select * from employee_demographics
where gender = 'Male'
order by employee_id ASC; -- gender = male and showing employee_id in ascending order. 




 