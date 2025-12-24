SELECT c.name as Customers
FROM Customers as c
LEFT JOIN Orders as O
ON c.id = o.customerId
WHERE o.customerId is NULL;


