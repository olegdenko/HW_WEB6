 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname AS teacher_name, s2.name AS subject_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
JOIN [groups] gr ON gr.id = s.group_id
JOIN teachers t ON t.id = s2.teacher_id
WHERE t.id = 1
GROUP BY t.fullname, s2.name
ORDER BY average_grade DESC;