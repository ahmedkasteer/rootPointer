SELECT * from products;

create table products (
	product_id INT,
    product_name VARCHAR(25),
    price DECIMAL(4, 2) NOT NULL -- using not null constraint so values can't be null at all. 
);
-- adding not null constraint to a table already in schema. 
ALTER TABLE products
modify price DECIMAL (4,2) NOT NULL;

select * from products;

insert into products 
values (104,"cookie", NULL); -- results in error since price is null and we set NOT NULL constraint above. 0 is acceptable but NULL is not. 

