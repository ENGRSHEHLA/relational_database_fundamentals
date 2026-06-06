-- Schema + sample data so this file can be run standalone (SQLite/Postgres compatible)
CREATE TABLE IF NOT EXISTS student (
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	major TEXT,
	age INTEGER
);

INSERT INTO student (student_id, name, major, age) VALUES
	(1, 'Alice', 'Comp Sci', 20),
	(2, 'Bob', 'History', 22),
	(3, 'Carol', 'Politics', 21),
	(4, 'Dave', 'Math', 23),
	(5, 'Eve', 'Comp Sci', 19)
	ON CONFLICT(student_id) DO NOTHING;

SELECT *
FROM student
WHERE major IN ('Politics', 'Comp Sci', 'History')
LIMIT 2;
-- WHERE student_id > 3 AND name <> 'Jack';