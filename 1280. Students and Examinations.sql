# Write your MySQL query statement below
SELECT St.student_id, student_name, Su.subject_name, Count(E.subject_name) AS attended_exams
FROM Students St
JOIN Subjects Su
LEFT JOIN Examinations E ON St.student_id = E.student_id AND Su.subject_name = E.subject_name
GROUP BY 1, 2, 3
ORDER BY 1;