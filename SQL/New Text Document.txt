/*
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).*/
=================================================
set @number = 21;
select repeat('* ', @number := @number - 1) from information_schema.tables;