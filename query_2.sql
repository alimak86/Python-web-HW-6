SELECT students.student_name, ROUND(AVG(marks.mark),2) FROM students
LEFT JOIN marks ON students.id = marks.student_id WHERE marks.subject_id = 5
GROUP BY students.student_name
ORDER BY ROUND(AVG(marks.mark),2) DESC LIMIT 1