-- Create Customers Table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    grade INTEGER
);

-- Insert Fictional Data
INSERT INTO customers (customer_id, customer_name, city, grade) VALUES
(1, 'John', 'New York', 120),
(2, 'Emma', 'Chicago', 90),
(3, 'Michael', 'New York', 80),
(4, 'Sophia', 'Boston', 150),
(5, 'David', 'New York', 200),
(6, 'Olivia', 'Seattle', 110);

-- Customers who belong to New York
-- OR customers having grade above 100
SELECT *
FROM customers
WHERE city = 'New York'
   OR grade > 100;

-- Customers who belong to New York
-- AND customers having grade above 100
SELECT *
FROM customers
WHERE city = 'New York'
  AND grade > 100;