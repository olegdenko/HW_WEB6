-- Знайти середній бал у групах з певного предмета.
SELECT s2.name, gr.name , ROUND(AVG(g.grade), 2) AS average_grade 
FROM grades g 
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
JOIN [groups] gr ON gr.id = s.group_id
WHERE s2.id = 8
GROUP BY gr.name, s2.name
ORDER BY average_grade DESC;