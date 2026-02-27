SELECT e1.name
FROM Employee e1, Employee e2
WHERE e1.id = e2.managerId 
GROUP BY e1.id
HAVING COUNT(e1.id) >= 5;