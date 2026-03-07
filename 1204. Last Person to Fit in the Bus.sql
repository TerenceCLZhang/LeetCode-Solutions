# Write your MySQL query statement below
SELECT a.person_name 
FROM Queue a
WHERE (
    SELECT SUM(b.weight)
    FROM Queue b
    WHERE b.turn <= a.turn
) <= 1000
ORDER BY a.turn DESC
LIMIT 1;