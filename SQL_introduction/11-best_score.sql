-- List the core and name of each record in second_table with a score higher than or equal to 10, ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
