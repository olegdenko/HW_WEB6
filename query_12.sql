-- Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT s.fullname AS student_name, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id
JOIN groups gr ON gr.id = s.group_id
WHERE gr.id = 2
  AND s2.id = 3
  AND g.day_of = (SELECT MAX(day_of) FROM grades WHERE student_id = s.id AND subject_id = s2.id);