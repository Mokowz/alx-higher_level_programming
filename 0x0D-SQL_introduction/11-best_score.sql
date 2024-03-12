-- script 11
-- lists score with more than 10
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;