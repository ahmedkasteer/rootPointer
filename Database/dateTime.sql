CREATE TABLE test(
	my_Date DATE,
    my_time TIME,
    my_datetime DATETIME
);

SELECT * from test;

insert into test
values(current_date(), current_time(), now()); -- current_date() returns current date and current_time returns current_time(), now returns time right now. these are all built in functions. 

SELECT * from test;

insert into test
values(current_date() - 1, NULL, NULL ); -- this returns yesterday. - 1 that is. 

insert into test
values(current_date() + 1 , NULL, NULL); -- this returns tomorrow from today's date, + 1 that is. 

DROP TABLE test;  -- since we don't need the table anymore, we have dropped it. this deletes the table. 


