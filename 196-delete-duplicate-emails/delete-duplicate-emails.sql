-- Write your PostgreSQL query statement below
DELETE FROM Person
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM Person
    )
    WHERE rn > 1
);
