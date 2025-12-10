-- check constraint
select * from employees;
-- to add check constraint when creating a new table use -contraint- followed by -variable name- then -check (condition)-
create table employee (
	employee_id int,
    first_name varchar(50),
	last_name varchar(50),
	hourly_pay decimal(5, 2),
	hire_date DATE, 
    constraint chk_hourly_pay check (hourly_pay >= 10.00 ) -- constraint chk_hourly_pay check (hourly pay > 10.00) used here. 
);

alter table employees
add constraint chk_hourly_pay check (hourly_pay >= 10.00); -- already given table applying check constraint use this. 

-- now inserting new value with hourly pay < 10 to see what happens. 
insert into employees
values (6, "ahmed", "kasteer", 5.00, "2023-01-07", +923127766554);
-- see? chk_hourly_pay violated error since we added 5.00 as hourly pay whereas we wanted it to be greater than 10.00
-- boom. can't add value. so error occured. go home. 

-- hence to fix it use hourly pay value >= 10.00
insert into employees
values (6, "ahmed", "kasteer", 10.00, "2023-01-07", +923127766554);
-- successfull!!!

-- to delete a check we can simply:
alter table employees
drop check chk_hourly_pay;
-- drops the check condition we added previously. 
