CREATE TABLE IF NOT EXISTS student(
    ROLL_NUM TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTERGER
);

INSERT INTO student(
    ROLL_NUM,
    NAME,
    ADDRESS,
    PHONE,
    AGE
)
VALUES
    ( '1', 'RAM', 'LONDON', '**********', 18),
    ( '2', 'JOHN', 'CHICAGO', '**********', 19),
    ( '3', 'JACK', 'NEW YORK', '**********', 18),
    ( '4', 'PHIL', 'CHICAGO', '**********', 20),
    ( '5', 'MIKE', 'LONDON', '**********', 20),
    ('6', 'JIM', 'DALLAS', '**********', 22);

SELECT * FROM student;
SELECT * FROM student WHERE ADDRESS = 'LONDON' AND AGE = 18;
SELECT * FROM student WHERE AGE = 20 OR NAME = 'MIKE';
SELECT * FROM student WHERE AGE = 20 AND (NAME = 'MIKE' OR 'PHIL');