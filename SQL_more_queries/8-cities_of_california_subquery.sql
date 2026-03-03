-- Cities of California
SELECT id, state_id, name
FROM hbtn_0d_usa.cities
WHERE name = 'California'
ORDER BY cities.id ASC;