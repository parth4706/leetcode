# Write your MySQL query statement below
SELECT Email
FROM person
GROUP BY email
HAVING COUNT(*) > 1;
