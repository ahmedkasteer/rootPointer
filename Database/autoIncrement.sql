-- auto increment attirbute 
create table transactions (
 transaction_id int primary key auto_increment, -- helps u automatically increment the column no, based on values inserted. 
 amount decimal (5, 2)
);

select * from transactions;

insert into transactions(amount) 
values (7.99); -- so for every value added, we have our transaction id incrementing by 1. 

alter table transactions
auto_increment = 1000; -- we can make the table start from increment by 1000 so each value added will result in 1001,1002,1003 and so on 

set sql_safe_updates = 0;

delete from transactions;

select * from transactions ;

insert into transactions(amount)
values (9.99);

-- result is: 

# transaction_id,  amount
-- 1000				3.99
-- 1001				4.99
-- 1002				5.99
-- 1003				6.99
-- 1004				9.99