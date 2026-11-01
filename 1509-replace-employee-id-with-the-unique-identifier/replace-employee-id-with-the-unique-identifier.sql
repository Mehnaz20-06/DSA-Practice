# Write your MySQL query statement below
SELECT emp.name , eu.unique_id
FROM Employees as emp
LEFT JOIN EmployeeUNI as eu
ON emp.id=eu.id;
