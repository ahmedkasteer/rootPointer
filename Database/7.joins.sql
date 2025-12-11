-- joins allow u to combine 2 tables or more if they have common column same data should be in both tables' columns. 
-- not necessarily same name of the column. 
select * from employee_demographics;
select * from employee_salary;

-- this gives us data from two tables that have same column name and present in both tables. basically the common of both including all data from both tables. 
select dem.employee_id, age, occupation
from employee_demographics as dem
inner join employee_salary as sal
on dem.employee_id = sal.employee_id;

-- outer joins includes left join or left outer join or right join or right outer join. 
select *
from employee_demographics as dem -- this our left table 
left join employee_salary as sal -- this our right table on which we joining. left table dominant.  
on dem.employee_id = sal.employee_id;

select *
from employee_demographics as dem -- this our left table 
right join employee_salary as sal -- this our right table on which we joining. right table dominant. 
on dem.employee_id = sal.employee_id;
-- ^^^^ above e.g if there are values in right table and no same values in left since right is dominant then there will be null in results. 

-- self join tie table to itself. 
select *
from employee_salary emp1
join employee_salary emp2
on emp1.employee_id + 1 = emp2.employee_id;

select emp1.employee_id as emp_santa, 
emp1.first_name as first_name_Santa, 
emp1.last_name as last_name_Santa, 
emp2.employee_id as emp_name, 
emp2.first_name as first_name_emp, 
emp2.last_name as last_name_emp  
from employee_salary emp1
join employee_salary emp2
on emp1.employee_id + 1 = emp2.employee_id;

-- joining multiple tables together so we joining three tables here, employee_salary has dept_id used to join department_id of parks_departments 
select *
from employee_demographics as dem
inner join employee_salary as sal
	on dem.employee_id = sal.employee_id
inner join parks_departments pd
	on sal.dept_id = pd.department_id;

select *
from parks_departments;
