/*
1.
SQL – Composer
table composer҅ 3 columns: userid | event | date,
event include enter/post/cancel
(1) what is the post success rate for each day in the last week?
*/

post success rate =  # of post/ # of enter

select 
      date, 
      Round(ifnull(SUM(CASE WHEN EVENT = "POST" 1 ELSE 0 END)/
                   SUM(CASE WHEN EVENT = "ENTER" 1 ELSE 0), 0),2)
FROM composer 
where Datediff(date, curdate()) < 7
group by 1




/*
table- user 4 columns: userid | date | country | dau_flag{0,
1dau_flag: daily active or not
what is the average number of post per daily active user by country today?
*/
               
obj = total posts / active users

select 
     country, 
     ROUND(ifnull(SUM(case when c.event="post" 1 ELSE 0 END)/
                  count(distinct c.users),0),2) AS AVE_POST
FROM 
     COMPOSER c
     JOIN USERS u ON c.userid = u.userid and c.date = u.date
WHERE u.dau_flag = "active" and u.date = curdate()
group by 1



/*
Table: date timestamp send_id receive_id
Question: What’s the fraction of users communicating to > 5 users in a day?
*/
 


               

               
               
               
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
(User can only confirm during the same day FB sent the confirmation message)

1. yesterday how many confirmation texts by country
*/




/*
2. Number of users who received notification every single day during the last 7 days.
*/



/*
3.confirmation rate in the past 30 days
*/
