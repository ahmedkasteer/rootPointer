set sql_safe_updates = 1; 

select * from products;

insert into products
values (104, "straw", 0.00),
	   (105, "napkin", 0.00),
       (106, "fork", 0.00),
       (107, "spoon", 0.00);

delete from products 
where product_id >= 104;
 -- to create a new table with default values. 
create table products(
product_id int,
product_name varchar(25),
price decimal(4, 2) DEFAULT 0.00
);

-- alter table to make default constraint
alter table products
alter price set default 0;
-- now inserting values, leaving out price for default is how we use it. no value = default. 
-- but since mentioning only 2 columns and not third, need to mention explicitly in the products() parentheses 
insert into products (product_id, product_name)
values (104, "straw"),
	   (105, "napkin"),
       (106, "fork"),
       (107, "spoon");
-- creating a new table with DEFAULT value of transaction of current time and date. 
create table transactions(
transaction_id int,
amount decimal (5, 2),
transaction_date datetime Default now()
);

select * from transactions;

insert into transactions(transaction_id, amount) -- adding first 2 columns, leaving third one empty for default value. 
values (2, 8.99); -- adding values by repeatedly changing these values. 

-- now dropping table cuz we done with example

drop table transactions;

