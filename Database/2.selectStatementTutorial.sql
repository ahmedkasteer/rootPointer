select first_name, last_name, birth_date, age, (age+10) * 10						-- age+10 will create new column adding calculations
from parks_and_recreation.employee_demographics;
#pemdas  			order of operations parentheses, exponent, multiplicaiton, division, addition, subtraction 

select distinct gender -- distinct allows us to give and show unique values in a column. 
from parks_and_recreation.employee_demographics;
