-- script 19
-- display hottest cities
SELECT city, AVG(value) as avg_temp 
FROM temperatures
WHERE month = 7 or month = 8
ORDER BY AVG(value) DESC
LIMIT 3;