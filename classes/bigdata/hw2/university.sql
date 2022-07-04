-- Clear tables
drop table if exists students;

drop table if exists course;

drop table if exists enrolled;

-- Create tables
CREATE TABLE students
(
	studentid INT NOT NULL PRIMARY KEY,
	gender TEXT,
    age INT,
    major TEXT,
    class TEXT
);

CREATE TABLE course
(
	courseid  INT,
	teacherid  INT,
    department TEXT,
	PRIMARY KEY(courseid,teacherid)
);

CREATE TABLE enrolled
(
	studentid  INT,
	courseid  INT,
    grade INT,
	PRIMARY KEY(studentid,courseid)
);

INSERT INTO students
VALUES
(1, "male", 25, "natural language processing", "NLP101"),
(2, "female", 25, "computer vision", "CV101");

INSERT INTO course
VALUES
(1, 1, "School of NLP"),
(10, 2, "School of CV");

INSERT INTO enrolled 
VALUES 
(1, 1, 100),
(2, 10, 100);
