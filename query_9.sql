SELECT subjects.subject_name, students.student_name FROM subjects LEFT JOIN marks ON subjects.id = marks.subject_id JOIN students ON students.id = marks.student_id WHERE students.id = 24