SELECT m.name
FROM Employee as e
LEFT JOIN Employee as m
ON e.managerId = m.id
GROUP BY e.managerId
HAVING COUNT(m.id) >= 5;


