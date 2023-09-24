-- Знайти список студентів у певній групі.
SELECT s.fullname as student_name
FROM [groups] g
JOIN students s ON s.group_id  = g.id
WHERE g.id = 3
ORDER BY student_name DESC;