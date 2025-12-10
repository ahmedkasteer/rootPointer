-- primary key can be applied to a column. must be both unique and not null
-- table can have only 1 primary key constraint

create table transactions (
transaction_id int primary key,
amount decimal (5,2)
);

select * from transactions;
-- alter table syntax for existing table to add primary key constraint 
alter table transactions
add constraint primary key (transaction_id); -- wont work here since we already defined primary_key when creating table. 

insert into transactions
values (1003, 11.99); -- populating table with same id will result in error since primary key constraint. 

-- so it gives us the amount value corresponding to the transaction ID 
select amount from transactions 
where transaction_id = 1003;