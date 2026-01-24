SELECT m.name
FROM Employee as e
JOIN Employee as m
ON e.managerID = m.id
GROUP BY e.managerID
HAVING COUNT(m.id) >= 5;
