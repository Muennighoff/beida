##### 思考


学生： 孟念 (Niklas Muennighoff)

I first created an SQL script that creates the three tables and adds a couple of sample rows.

Then I created the UI with tkinter with the following functionalities:
- Add student to student db
- Add course to course db
- Add grade to enrolled db
- Retrieve student grade from course

Error messages are displayed at the bottom and no extensive error checking is performed. This way, debugging is outsourced to the user.

Below is an example image of the interface:


![UI](./university_ui.jpg?raw=true "University DB UI")



Further extensions could be:
- Improve the UI - Alignments; Coloring; Sizes
- Additional retrieval functionalities not just grade, but also user name etc
- More databases, such as teacher
- More columns in the databases, such as student name

