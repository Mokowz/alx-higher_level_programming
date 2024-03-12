-- script 15
-- list number of records with the same score
SELECT score, count(*) as number FROM second_table
ORDER BY count(*);