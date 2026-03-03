-- List all cities with their states
SELECT cities.id,
       cities.name AS city,
       states.name AS state
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;