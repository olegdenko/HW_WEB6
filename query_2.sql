-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT s2.name, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade 
FROM grades g 
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
WHERE s2.id = 3
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;