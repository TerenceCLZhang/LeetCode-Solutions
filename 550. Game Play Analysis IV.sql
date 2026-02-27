WITH First_Day AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(AVG(CASE WHEN a.player_id IS NOT NULL THEN 1 ELSE 0 END), 2) AS fraction
FROM First_Day f
LEFT JOIN Activity a ON f.player_id = a.player_id 
AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);