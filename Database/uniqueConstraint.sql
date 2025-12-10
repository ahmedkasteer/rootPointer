CREATE TABLE products(
	product_id INT,
    product_name VARCHAR(25) UNIQUE, -- all these names of products should be unique. 
    price DECIMAL(4, 2) -- 4 digits and precision of 2 decimal places. 
);
-- if we forget mentioning unique then we can: 
ALTER TABLE products
ADD CONSTRAINT
UNIQUE(product_name);

SELECT * FROM products;

truncate products;  -- deletes all rows and columns 

insert into products 
values 
	(100, "hamburger", 3.99),
	(101, "fries", 1.99),
    (102, "soda", 0.99),
    (103, "icecream", 2.99); -- inserting values in our table. 
--  (104, "fries", 1.75);  <- this will result in duplicate since we used unique phrase and fries already exist. 


