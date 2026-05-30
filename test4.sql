CREATE TABLE IF NOT EXISTS salesman(
    SALESMAN_ID TEXT,
    NAME TEXT,
    CITY TEXT,
    COMISSION TEXT
);

INSERT INTO salesman(
    SALESMAN_ID,
    NAME,
    CITY,
    COMISSION
)
VALUES(
    '5001', 'JAMES', 'NEW YORK', '0.15'),
    ('5002', 'NEAL', 'PARIS', '0.13'),
    ('5003', 'LAUREN', 'SAN JOSE', '0.12'),
    ('5007', 'PAUL', 'ROME', '0.13'),
    ('5005', 'ALEX', 'LONDON', '0.11'),
    ('5006', 'LYON', 'PARIS', '0.14');

CREATE TABLE IF NOT EXISTS customer(
    CUSTOMER_ID TEXT,
    CUSTOMER_NAME TEXT,
    CITY TEXT,
    GRADE TEXT,
    SALESMAN_ID TEXT
);

INSERT INTO customer(
    CUSTOMER_ID,
    CUSTOMER_NAME,
    CITY,
    GRADE,
    SALESMAN_ID
)
VALUES(
    '3002', 'NICK', 'NEW YORK', '100', '5001'),
    ('3007', 'BRAD', 'NEW YORK', '200', '5001'),
    ('3005', 'GRAHM', 'CALIFORNIA', '200', '5002'),
    ('3008', 'JULIAN', 'LONDON', '300', '5002'),
    ('3004', 'FABIAN', 'PARIS', '300', '5006'),
    ('3009', 'CAMERON', 'BERLIN', '100', '5003'),
    ('3003', 'JOSIE', 'MOSCOW', '200', '5007'),
    ('3001', 'JOHNSON', 'LONDON', '', '5005');

CREATE TABLE IF NOT EXISTS orders(
    ORDER_NUM TEXT,
    PURCHASE_AMT TEXT,
    ORDER_DATE TEXT,
    CUSTOMER_ID TEXT,
    SALESMAN_ID TEXT
);

INSERT INTO orders(
    ORDER_NUM,
    PURCHASE_AMT,
    ORDER_DATE,
    CUSTOMER_ID,
    SALESMAN_ID
)
VALUES(
    '70001', '150.5', '2012-10-05', '3005', '5002'),
    ('70009', '270.65', '2012-09-10', '3001', '5001'),
    ('70002', '65.26', '2012-10-05', '3002', '5003'),
    ('70004', '110.5', '2012-08-17', '3009', '5007'),
    ('70007', '948.5', '2012-09-10', '3005', '5005'),
    ('70005', '2400.6', '2012-07-27', '3007', '5006');

SELECT * FROM customer, orders, salesman;

SELECT customer.customer_name, salesman.name, salesman.city FROM customer JOIN salesman ON
customer.city = salesman.city;

SELECT customer.customer_name, salesman.name FROM customer JOIN salesman ON customer.salesman_id =
salesman.salesman_id;

SELECT orders.order_num, customer.customer_name, orders.customer_id, orders.salesman_id FROM orders
JOIN customer ON orders.customer_id = customer.customer_id JOIN salesman ON orders.salesman_id =
salesman.salesman_id WHERE customer.city <> salesman.city;

SELECT orders.order_num, customer.customer_name FROM orders JOIN customer ON orders.customer_id =
customer.customer_id;

SELECT customer.customer_name AS "customer", customer.grade AS "grade" FROM orders JOIN salesman ON
orders.salesman_id = salesman.salesman_id JOIN customer ON orders.customer_id = customer.customer_id
WHERE customer.grade IS NOT NULL;

SELECT customer.customer_name AS "customer", customer.city AS "city", salesman.name AS "salesman",
salesman.comission FROM customer JOIN salesman on customer.salesman_id = salesman.salesman_id WHERE
salesman.comission BETWEEN 0.12 AND 0.14;

SELECT * FROM customer JOIN orders ON customer.customer_id = orders.customer_id WHERE
orders.order_date = '2012-10-05';