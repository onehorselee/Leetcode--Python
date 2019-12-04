/* composer 
https://drive.google.com/file/d/1JwZzaUnFWd5YPSf9nuXilvne1lpDQFiZ/view */
SELECT date,
ROUND(IFNULL(SUM(case when event="post" then 1 else 0 end)/
             SUM(CASE WHEN event='enter' then 1 else 0 end), 0), 2) as success_rate
FROM 
    composer
WHERE 
    datediff(curdate(), date) <=7
GROUP BY 1