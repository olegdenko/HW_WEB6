-- Список курсів, які певному студенту читає певний викладач.
SELECT s2.name AS course_name
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
JOIN teachers t ON t.id = s2.teacher_id
WHERE s.id = 15
  AND t.id = 3
GROUP BY s2.name
ORDER BY course_name;