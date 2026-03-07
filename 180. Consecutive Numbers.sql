# Write your MySQL query statement below
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b ON a.Id = b.Id + 1 AND a.num = b.num
JOIN Logs c ON b.Id = c.Id + 1 AND b.num = c.num;