-- ists the number of records with the same score
-- ists the number of records with the same score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
HAVING COUNT(score);
