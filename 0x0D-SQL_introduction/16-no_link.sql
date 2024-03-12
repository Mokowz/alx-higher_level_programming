-- script 16
-- list rows without name value
SELECT score, name FROM second_table
WHERE name <> ''
ORDER BY score DESC;