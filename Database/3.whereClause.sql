-- where clause
select * from employee_salary
where first_name = 'Leslie';

select *from employee_salary
where salary >= 50000;  

select *from employee_demographics
where gender != "Female";

select *from employee_demographics
where birth_date > '1985-01-01';

-- AND OR NOT -- logical operators
select *from employee_demographics
where birth_date > '1985-01-01'
and gender = 'male';

select *from employee_demographics
where birth_date > '1985-01-01'
or not gender = 'male';
-- this is isolated conditional statement which can be true or not due to OR in between them.
select *from employee_demographics
where (first_name = 'Leslie' and age = 44) or age > 55;
-- like statement where % means anything and _ means specific value 
-- so anything or specific values can be printed using like 'Jerr%' or '%er%' <<-- any name can come before er and followed by er. 
select *from employee_demographics
where first_name like 'a%';

-- now using _ means specific no of values. _ means 1 char, __ means 2 char and so on. 
select * from employee_demographics;
-- where first_name like 'a____'; -- 3 underscores gives 3 letters after A name so it's a.ndy "ANDY".
-- we can also combine _ and % to make sure it has _ (specific no of chars) followed by any number of characters...'
select * from employee_demographics
where first_name like "A___%";
-- doing it on birthdates will give only year we want and then result showing employees born in that year. 
select * from employee_demographics
where birth_date like "1989%";


