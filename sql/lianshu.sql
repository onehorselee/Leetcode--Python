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


/* confirmation by country yesterday*/
SELECT country, count(*)
FROM sms_message
WHERE type="confirmation" and DATEDIFF(CURDATE, DATE)=1
GROUP BY 1
ORDER BY 2 DESC


/* whats' the fraction of users communicating to > 5 users in a day? 
col: date, timestamp, send_id, receive_Id
table: messager
*/

SELECT 
    date, 
    round(sum(CASE WHEN num_contracts >= 5 then 1 else 1 end)/COUNT(user_id)) as fraction
from 
(
    select date, user_id, COUNT(DISTINCT user_id2) as num_contacts
    from 
        (select date, send_id as user_id, receive_id as user_id2 from messager
        UNION ALL  
        select date, receive_id as user_id, send_id as user_id2 from messager) T1
        group by 1, 2
) T2
group by 1

/*
follow-up:  
fraction of users who reponsed within a minute of a day 
*/



/*
SQL — sms_message (fb to users)
| date | country | cell_numer | carrier | type
|2018-12-06 | US | xxxxxxxxxx | verizon | confirmation (ask user to confirm)
|2018-12-05 | UK | xxxxxxxxxx | t-mobile | notification

confirmation (users confirmed their phone number)
|date | cell_number |
(User can only confirm during the same day FB sent the confirmation message) */

/* 1. yesterday how many confirmation texts by country */

select 
    country,
    count(*)
from (
    select * from sms_message s 
    LEFT JOIN confirmation c 
    where s.cell_number = c.cell_number and datediff(curdate(), date)=1 and s.type="confirmation"
    ) t1
group by 1
order by 2 DESC 

/*2. Number of users who received notification every single day during the last 7 days.  */
select 
    date, 
    count(distinct numbers) as "num_users"
from sms_message s 
where s.type = "notifications" and datediff(curdate(), date) <=6
group by 1


/*找出每个国家每个carrier的confirmation 总数。*/
select
country, 
carrier,
count(*) as "confirmation_num"
from sms_message
where type="confirmation"
group by country, carrier
order by 1, 2

/* 过去30天的confirmation rate */
select 
    T1.date, 
    round(ifnull(num_confirmations/num_send,0),2) as confirmation_rate
from 
    (select 
        date, count(*) as num_confirmations
    from confirmation where datediff(curdate(), date) <=30 
    group by 1) T1
    join 
    (select 
        date, sum(case when type="confirmation" then 1 else 0 end) as num_send
    from sms_message where datediff(curdate(),date) <=30
    group by 1) T2
    on t1.date = t2.date
group by 1


/* On dec 06th, overall confirmation rate. */


/*
ad4ad: date, user_id, event(impression, click, create_ad), unit_id, cost, spend，
记得还有一列，可能是ad_id，event是create_ad对应的行才有数值
users: user_id, country, age
*/



/*1. last 30 days, by country, total spend (问的是facebook的spend就是表里的cost） of the product*/
select 
    country, 
    sum(ifnull(spend,0)) as total_spend, 
from ad4ad a 
left join users u on a.user_id = u.user_id
where datediff(curdate(),date)<=30 
group by 1

/*2. how many impressions before users create an ad given an unit?*/
select 
    a1.user_id, 
    a1.unit_id, 
    sum(case when a1.event="impression" then 1 else 0) as num_impressions
from (
    select distinct(user_id, unit_id) 
    from ad4ad a1 where a1.event = "create_ad"     
    left join ad4ad a2 on a1.user_id = a2.user_id and a1.unit_id = a2.unit_id)
group by 1, 2

/*3. avg number of impressions per user per item before user creates ad*/
select 
    unit_id, 
    sum(num_impressions)/count(distinct user_id)
from 
    (select 
    a1.user_id, 
    a1.unit_id, 
    sum(case when a1.event="impression" then 1 else 0) as num_impressions
from (
    select distinct(user_id, unit_id) 
    from ad4ad a1 where a1.event = "create_ad"     
    left join ad4ad a2 on a1.user_id = a2.user_id and a1.unit_id = a2.unit_id)
group by 1, 2) t1
group by 1

/*
SQL — SPAM
-- Table: user_actions
-- ds(date, String) | user_id | post_id |
     action ('view','like','reaction','comment','report','reshare') |
    extra (extra reason for the action, e.g. 'love','spam','nudity')

/*-- Introduce a new table: reviewer_removals, 
  -- ds(date, String) | reviewer_id |post_id */


/*-- Q1: how many posts were reported yesterday for each report Reason?*/
SELECT 
    extra AS reason
    DISTINCT(post_id)
FROM user_actions
WHERE action = "report" and DATEDIFF(CURDATE(), ds)=1
GROUP BY 1


/* Q2 --please calculate what percent of daily content that users view on FB is actually spam?
      --no need to consider if the removal happen at the same post date or not.
*/
select 
    user_id,
    post_id,
    ifnull(sum(case when extra="spam" then 1 else 0 end)/count(*),0) as spam_percentage
from user_actions
where action="view"
group by 1

/*-- Q3: How to find the user who abuses this spam system?*/
-- users that report spam but which are not spams, 
-- (not spam) / reported spam - fake_spam_rate
select 
    users_id,
    ifnull(round(sum(case if review_id is null then 0 else 1 end)/count(distinct u.post_id),2),0) as fake_spam_rate
from user_actions u    
left join reviewer_removals  r on u.post_id = r.post_id
where u.action="report"
group by 1
order by 2 DESC



/*SQL — given table with: (user, group, time, displays, clicks) for a payment page.
5) how to identify click but not displays*/

/*1) # of clicks and displays in given day*/

/*2) click through rate,*/


/*3) click through rate for each group,*/

/*4) group 1 click rate: 10%, group 2: 15%, think about possible differences, group 3 click rate
150%, think about possible reason,*/





/**/
