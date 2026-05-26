CREATE TABLE IF NOT EXISTS products(
    PRODUCT_ID TEXT,
    PRODUCT_NAME TEXT,
    SUPPLY_ID TEXT,
    CATAGORY_ID TEXT,
    UNIT_TEXT,
    PRICE_REAL
);

INSERT INTO products(
    PRODUCT_ID,
    PRODUCT_NAME,
    SUPPLY_ID,
    CATAGORY_ID,
    UNIT_TEXT,
    PRICE_REAL
)
VALUES(
    '1','COKE','3','4', 25, 20),
    ('2','CHEETOS','4','1', 40, 22),
    ('3','FANTA','2','4', 26, 18),
    ('4','DORITOS','1','1', 45, 24),
    ('5','APPLES','6','10', 10, 15
);

SELECT * FROM products;

SELECT COUNT(PRODUCT_ID) AS product_count FROM products;

SELECT AVG(PRICE_REAL) AS average_price from products;

SELECT SUM(PRICE_REAL) AS price_sum from products;