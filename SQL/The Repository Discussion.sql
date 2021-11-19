/*
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks. Grades contains the following data: Grade, Max_mrks, Min_Marks

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.
*/

/*Variant 1*/

SELECT Students.Name, Grades.Grade, Students.Marks FROM Students INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark WHERE Grades.Grade > 7 ORDER BY Grades.Grade DESC, Students.Name ASC;
SELECT null, Grades.Grade, Students.Marks FROM Students INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark WHERE Grades.Grade <= 7 ORDER BY Grades.Grade DESC, Students.Marks ASC;

/*Variant 2*/

SELECT IF (Grades.Grade > 7, Students.Name, NULL) AS Sname, Grades.Grade, Students.Marks FROM Students 
INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark
ORDER BY Grades.Grade DESC, Sname ASC, Students.Marks ASC;

/* Variant 3*/
SELECT 
    CASE
        WHEN Grades.Grade > 7
        THEN Students.Name
        WHEN Grades.Grade <= 7
        THEN NULL
    END, Grades.Grade, Students.Marks FROM Students INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark ORDER BY Grades.Grade DESC, Students.Name ASC, Students.Marks ASC;