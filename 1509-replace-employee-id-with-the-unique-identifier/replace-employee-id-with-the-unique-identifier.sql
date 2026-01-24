SELECT u.unique_id as unique_id ,e.name as  name
FROM Employees as e
LEFT JOIN EmployeeUNI as u
on e.id = u.id;