SELECT a.id as id
FROM Weather e
JOIN Weather a
ON DATEDIFF(a.recordDate, e.recordDate) = 1
WHERE a.temperature > e.temperature;