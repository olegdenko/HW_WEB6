-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.fullname, g.grade
FROM grades g
JOIN students ON students.id = g.student_id
JOIN subjects ON subjects.id = g.subject_id
JOIN groups ON groups.id = students.group_id
WHERE subjects.id = 3
  AND groups.id = 1;