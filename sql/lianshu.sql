/* composer 
https://drive.google.com/file/d/1JwZzaUnFWd5YPSf9nuXilvne1lpDQFiZ/view 
*/
SELECT 
    date,
    ROUND(IFNULL(SUM(case when event="post" then 1 else 0 end)/
                SUM(CASE WHEN event='enter' then 1 else 0 end), 0), 2) as success_rate
FROM 
    composer
WHERE 
    datediff(curdate(), date) <=7
GROUP BY 1



select 
    country,
    round(IFNULL(sum(case when c.event="post" then 1 else 0 end)/
                count(distinct u.userid),0),2) as avg_posts
from 
    user u
    left join composer c 
    on u.userid = c.userid and u.date = c.date
where date = curdate() and u.dau_flag = 1
group by 1



