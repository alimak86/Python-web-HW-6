-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) UNIQUE NOT NULL,
    student_group INTEGER,
    FOREIGN KEY (student_group) REFERENCES groups(id)
      ON UPDATE CASCADE
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: proffessors
DROP TABLE IF EXISTS proffessors;
CREATE TABLE proffessors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proffessor_name VARCHAR(255) UNIQUE NOT NULL
);


-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(255) UNIQUE NOT NULL,
    proffessor_id INTEGER,
    FOREIGN KEY(proffessor_id) REFERENCES proffessors (id)
);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    mark INTEGER,
    FOREIGN KEY(student_id) REFERENCES students (id)
    FOREIGN KEY(subject_id) REFERENCES subjects (id)
);