SELECT students.student_name, groups.group_name FROM students LEFT JOIN groups ON students.student_group = groups.id WHERE groups.id = 2