-- Знайти список курсів, які відвідує студент.
SELECT s2.name AS course_name
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
WHERE s.id = 3
GROUP BY s2.name
ORDER BY course_name;