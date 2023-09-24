-- Знайти які курси читає певний викладач.
SELECT s.name AS course_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 5
GROUP BY s.name, t.fullname
ORDER BY course_name DESC;