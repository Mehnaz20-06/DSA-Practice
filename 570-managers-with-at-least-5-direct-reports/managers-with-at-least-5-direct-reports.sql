SELECT m.name
FROM Employee as e
JOIN Employee as m
ON e.managerID = m.id
GROUP BY m.id ,m.name 
HAVING COUNT(e.id) >= 5;