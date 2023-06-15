SELECT groups.group_name, ROUND(AVG(marks.mark),2), subjects.subject_name FROM students
LEFT JOIN groups ON students.student_group = groups.id LEFT JOIN marks ON students.id = marks.student_id LEFT JOIN subjects ON subjects.id = marks.subject_id WHERE marks.subject_id = 5 
GROUP BY groups.group_name
ORDER BY ROUND(AVG(marks.mark),2) DESC