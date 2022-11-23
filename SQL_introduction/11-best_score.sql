-- script that lists all recoreds with 'score >= 10' in the 'second_table' in your MYSQL server
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
