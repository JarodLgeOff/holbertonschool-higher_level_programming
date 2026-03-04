-- List the score and name of each record in second_table, ordered by score, but only if the name is not NULL
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
