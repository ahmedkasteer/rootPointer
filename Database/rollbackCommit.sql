-- autocommit, commit and rollback 
-- set autommit = off; this will turn off automatic saving 
-- commit will be used to make a safepoint so all changes made upto commit will be stored only.
-- if you accidentally modified the data, use rollback to gather previous changes from commit. 
-- demonstration:
/* 
SET AUTOCOMMIT = OFF;
SELECT * FROM employees
DELETE FROM employees
yeap. entire rows deleted. 
but... if we did this:
SELECT * FROM employees;
COMMIT;
DELETE FROM employees; <- here we have deleted but notice we used commit to save previous changes then, 
if we use:
ROLLBACK;
the deleted rows and columns will be reverted and you can re-display them:
SELECT * FROM employees
 this is just like undo/redo feature on a texteditor. we just manually save everything after setting autocommit to off
 and then save changes manually using COMMIT; phrase. 
 Thas all folks. 
 