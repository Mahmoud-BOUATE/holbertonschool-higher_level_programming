-- Number by score
SELECT DISTINCT score, name
FROM second_table
where name IS NOT NULL
ORDER BY score DESC;