-- Create Employee table
CREATE TABLE Employee (
    Emp_ID INTEGER PRIMARY KEY,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Gender TEXT,
    Department TEXT,
    Designation TEXT,
    Salary REAL,
    Hire_Date DATE,
    Email TEXT,
    Phone TEXT
);

-- Insert sample data
INSERT INTO Employee
VALUES
(101, 'Rahul', 'Sharma', 'Male', 'IT', 'Software Engineer', 65000, '2022-01-15', 'rahul@company.com', '9876543210'),
(102, 'Priya', 'Verma', 'Female', 'HR', 'HR Manager', 75000, '2021-05-10', 'priya@company.com', '9876543211'),
(103, 'Amit', 'Singh', 'Male', 'Finance', 'Accountant', 55000, '2020-08-20', 'amit@company.com', '9876543212'),
(104, 'Neha', 'Gupta', 'Female', 'Marketing', 'Marketing Executive', 60000, '2023-03-12', 'neha@company.com', '9876543213');

-- Retrieve all employee details
SELECT * FROM Employee;