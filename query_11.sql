-- Середній бал, який певний викладач ставить певному студентові.
SELECT t.fullname AS teacher_name, s.fullname AS student_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
JOIN teachers t ON t.id = s2.teacher_id
WHERE t.id = 2
  AND s.id = 50
GROUP BY t.fullname, s.fullname
ORDER BY teacher_name, student_name;