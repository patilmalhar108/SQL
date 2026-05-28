-- Create Employees Table
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    department TEXT,
    salary INTEGER
);

-- Insert Fictional Data
INSERT INTO employees (emp_id, emp_name, department, salary) VALUES
(1, 'Alice', 'HR', 45000),
(2, 'Bob', 'IT', 60000),
(3, 'Charlie', 'Finance', 55000),
(4, 'David', 'IT', 70000),
(5, 'Eva', 'HR', 50000),
(6, 'Frank', 'Marketing', 48000);

-- Query to Get Company Employee Details
SELECT 
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    COUNT(DISTINCT department) AS total_departments,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees;