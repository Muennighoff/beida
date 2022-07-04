--Course Management Systems

--test creating students table
DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students(
id integer,
name text NOT NULL,
gender text NOT NULL,
age integer NOT NULL,
class text NOT NULL,
grade integer);


-- test inserting students data
INSERT INTO students (id,name,gender,age,class,grade) 
VALUES 
(1, "Tony","male",18,"SQL",1),
(2, "Amy","female",17,"Python",2),
(3, "Mike","male",19,"Java",2),
(4, "Loki","male",17,"Python",3),
(5, "Luna","female",17,"C++",1);


-- test inserting data with null field
INSERT INTO students (id,name,gender,age,class,grade) 
VALUES (6, "NoName","male",18,"SQL",NULL);


-- test selecting data
SELECT * FROM students WHERE class = 'Python';


-- test updating data
UPDATE students SET grade = 3 WHERE class = 'Python';


-- test deleting data
DELETE FROM students WHERE grade is NULL;


-- test creating class table
DROP TABLE IF EXISTS class;
CREATE TABLE IF NOT EXISTS class(
class_id integer,
class_name text NOT NULL,
lecturer text NOT NULL,
credit integer );


-- test inserting class data
INSERT INTO class (class_id,class_name,lecturer,credit) 
VALUES 
(1, "Python","Jobs",4),
(2, "Java","Lucas",5),
(3, "SQL","Kimi",3),
(4, "C++","Messi",5);


-- test creating enrolled table
DROP TABLE IF EXISTS enrolled;
CREATE TABLE IF NOT EXISTS enrolled(
student_id integer,
class_id integer,
credit integer,
score integer,
primary key(student_id,class_id));


-- test inserting enrolled data
INSERT INTO enrolled (student_id,class_id,credit,score) 
VALUES 
(1, 3, 3, 80),
(2, 1, 4, 85),
(3, 2, 5, 93),
(4, 1, 4, 85),
(5, 4, 5, 98);


-- test joint selection
select students.id, students.name, class.lecturer 
FROM students, class WHERE students.class = class.class_name;


-- test nested join
SELECT id, name, gender, age, grade, class_name,  score
FROM students s 
inner join
(
select student_id, class_name, score 
from class c
inner join 
enrolled e 
on c.class_id = e.class_id
) tc
on s.id = tc.student_id
Order by name, score DESC;


-- test simple join selection
select students.id, students.name, class.lecturer 
FROM students, class 
WHERE students.class = class.class_name;


select s.id, s.name, c.lecturer 
FROM students s, class c WHERE s.class = c.class_name;


-- test join selection
select s.id, s.name,  s.gender, s.age, s.grade, c.class_name, c.lecturer, e.score 
FROM students s, class c, enrolled e 
WHERE c.class_id = e.class_id and s.id = e.student_id;


-- test join selection
select DISTINCT s.id, s.name,  /*s.gender, s.age, s.grade,*/ c.class_name, c.lecturer, e.score 
FROM students s, class c, enrolled e 
WHERE c.class_id = e.class_id and s.id = e.student_id 
Order by s.grade, s.name, e.score DESC;

