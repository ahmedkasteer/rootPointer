SET SQL_SAFE_UPDATES = 0; 					-- setting safe updates to null to update our table's attributes set to 1 after update

UPDATE employees						-- in order to update a column value. we can use UPDATE - SET - WHERE 
SET hourly_pay = 10.25
WHERE employee_id = 6;

Update employees
set hire_date = null
where employee_id = 6;

SELECT * 
from employees;

-- warning. in order to update all column values of all rows. don't use where conditional clause. 
/* UPDATE employees
set hire_date = null
*/
 
Delete from employees 		-- will delete all rows if we just type this. 		
WHERE employee_id = 6;		-- deletes row of employee id 6. 5 employees remaining. 

-- done. 

