CREATE TABLE IF NOT EXISTS resturant(
    NAME TEXT,
    NEIGHBORHOOD TETX,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);

INSERT INTO resturant(
    NAME,
    NEIGHBORHOOD,
    CUISINE,
    REVIEW,
    PRICE,
    HEALTH
)
VALUES(
    'PETER', 'BROOKLYN', 'STEAK', 4.4, '$$$$', 'A'),
    ('JOHNGRO', 'MIDTOWN', 'KOREAN', 3.5, '$$', 'A'),
    ('POCHA', 'MIDTOWN', 'PIZZA', 4.0, '$$$', 'B'),
    ('LIGHTHOUSE', 'QUEENS', 'CHINESE', 3.9, '$', 'A'),
    ('MINCA', 'DOWNTOWN', 'AMERICAN', 4.6, '$$$', ''),
    ('MAREA', 'CHINATOWN', 'CHINESE', 3.0, '$$', ''),
    ('DIRTY CANDY', 'UPTOWN', 'ITALIAN', 4.9, '$$$$', 'B'),
    ('DIFARA PIZZA', 'BROOKLYN', 'PIZZA' 3.8, '$$', 'A'),
    ('GOLDEN UNICORN', 'UPTOWN', 'ITALIAN', 3.8, '$$', 'A');

--DISTINCT NEIGHBORHOOD
SELECT DISTINCT neighborhood FROM resturant;

--DISTINCT CUISINE TYPE
SELECT DISTINCT cuisine FROM resturant;

--CHINESE TAKEOUT OPTIONS
SELECT * FROM resturant WHERE cuisine = 'chinese';

--RESTURANT WITH REVIEWS 4 AND MORE
SELECT * FROM resturant WHERE review >= 4.0;

--ITALIAN RESTURANTS WITH $2-$3
SELECT * FROM resturant WHERE cuisine = 'italian' AND price IN ('$$', '$$$');

--RESTURANTS WITH EXACTLY $3
SELECT * FROM resturant WHERE price = '$$$';

--RESURANT NAME CONTAINS 'CANDY'
SELECT * FROM resturant WHERE name LIKE '%candy';

--RESTURANT IN MIDTOWN, DOWNTOWN, AND CHINATOWN
SELECT * FROM resturant WHERE neighborhood IN ('midtown', 'downtown', 'chinatown');

--RESTURANT WITH NULL HEALTH VALUES
SELECT * FROM resturant WHERE health = '' OR health IS NULL;

--TOP 4 RESTURANTS BASED ON REVIEWS
SELECT * FROM resturant ORDER BY review DESC LIMIT 4;