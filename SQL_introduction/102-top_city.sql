-- script that displays the top 3 of cities temp during July and August ordered by temp (desc)
SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
