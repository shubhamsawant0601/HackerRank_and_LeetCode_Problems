/*
Write a query calculating the amount of error (i.e.: average monthly salaries), and round it up to the next integer.
*/

select ceil(avg(salary) - avg(replace(salary, "0", ""))) from employees