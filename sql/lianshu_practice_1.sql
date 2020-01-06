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
*/

/*1) # of clicks and displays in given day*/
select display, click
from table where time=""

/*2) click through rate,*/


/*3) click through rate for each group,*/

/*4) group 1 click rate: 10%,
 group 2: 15%, think about possible differences,
 group 3 click rate
150%, think about possible reason,*/


/*5) how to identify click but not displays*/





/**/




-- SQL的话给了employee, department等四个表，但是问到的两个问题只用到了employee和department两个表。
-- Employee表有employee_id, first_name, second_name, salary, department_id五个fields，
-- department表有id, department_name两个fields。

-- SQL一：Find all department_name which the total salary of this department is larger than 40000.
SELECT d.Department_name
FROM Employee e JOIN Department d
ON e.Department_id = d.Department_id
GROUP BY d.Department_name
HAVING SUM(e.Salary) > 40000

-- SQL二：Find the employee in each department who has the max salary and print their names and salaries.
SELECT d.Name AS Department, e.Name AS Employee, e.Salay
FROM Department d JOIN Employee e
ON d.Department_id = e.Department_id AND e.Salary = (
  SELECT MAX(Salary)
  FROM Employee e2
  WHERE e2.Department_id = d.Department_id)


SELECT CONCAT(e.first_name,'', e.second_name) AS name, e.salary
FROM employee e JOIN department d
ON e.department_id = d.department_id
WHERE e.salary, d.department_id IN
( SELECT MAX(e.salary),  d.department_id
  FROM employee e JOIN department d
  ON e. Department_id = d.department_id
  GROUP BY d.department_id)

-- 问题一: Find the percentage of the customer who at least puchase 1 product.
SELECT COUNT(DISTINCT Sales.CustomerId) / COUNT(DISTINCT Customer.CustomerId)
FROM Sales, Customer

-- 问题二: Find (2015 total sales revenue / 2014 total sales revenue) - 1 for all the stores..

SELECT StoreId, SUM(IF(YEAR(Sales_date) = '2015', revenue, 0)) / SUM(IF(YEAR(Sales_date) = '2014', revenue, 0)) - 1
FROM Sales
GROUP BY StoreId

-- tables:
-- customers: id, name, birthday, gender
-- stores: id, state, area_squarefeet
-- product: id, name,....
-- sale: product_id, store_id, customer_id ...


-- 1. Percentage of male in customers
SELECT SUM(CASE WHEN gender = 'male' THEN 1 ELSE 0 END) / COUNT(*)
FROM Customer

-- 2. Percentage of customers who has at least 1 product
SELECT SUM(CASE WHEN product_id IS NULL THEN 0 ELSE 1 END) / COUNT(*) as ratio
FROM(
      SELECT c.name, product_id
      FROM customers c LEFT JOIN sale s
      ON c.id = s.customer_id
      GROUP BY c.id
    ) temp ;

-- 3. how many distinct states are all the store located -- count(distinct state)
SELECT COUNT(DISTINCT(state))
FROM stores

-- 3. count the product having at least 5 unit orders
SELECT COUNT (*)
    FROM
    ( SELECT product_id
      FROM sale
      GROUP BY product_id
      HAVING SUM(unit_order) >= 5) temp

-- 4. how many stores are having more than 26000 area sqrt, count by state basis
SELECT state, COUNT(id)
FROM stores s
WHERE area_squarefeet > 26000
GROUP BY state

-- 5. print out the oldest and youngest customer's birthday on gender level
SELECT gender, MIN(birthday), MAX(birthday)
FROM customers
GROUP BY gender

-- sql part： 4 or 5 questions. given 4 tables 产品，销售，客户, etc. cannot remember all the questions
-- * 找到最多的first name是什么

SELECT c.First_name
FROM Customer c
GROUP BY c.First_name
ORDER BY COUNT(*) DESC
LIMIT 1

-- * 找到前三销量的产品类别是什么
SELECT o.name,  AS Cnt
FROM Orders o
GROUP BY o.product_name
ORDER BY COUNT(*) DESC
LIMIT 3

-- * 购买了某两种产品的客户id是什么



第二轮sql也很简单，还是产品销售那四套表。 我都没做到需要join四个表的哈哈哈。
总结一下四题：
1. 考了count，
2. 忘了
3. order by xxx limit  
4. 就是算一下利润百分比，萨姆(销售-成本）/萨姆 销售



/*
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=570831&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
Python部分很简单：
1. 给一个数字列表且里面有None，重新输出一遍把None位置的数用前面存在的数代替。a = [1, None, 2, None, None, 5, Ne]
2. 给一个数字列表且某些数字重复，给出每个数字还需要加进多少个才能使得列表里每个数字都一样多。nums = [1, 3, 4, 1, 7, 8, 3 , 2, 4, 5, 7, 2, 3, 5, 6, 4, 2, 8, 5]
3. Average word length of a list of words。注意对每个word做.strip()
4. 给两个包含数字的列表，求两个列表里不重复的数字，不用在意输出顺序。list((set(a).union(set(b))).difference(set(a).intersection(set(b))))



SQL：
1. 有fat_flag 和 另外一个flag的products，总之就是join两个表A和B 然后on的时候除了id, 再加上对与B表的两个flag的限制条件
2. 选出single media的products（还是什么其他的table，不是重点），point在single media：这个column有不同的值，e.g. SEO  |   SEO, Ads, website | Ads, website。 single media就是用like 语句来筛选一下就好
3. promotion ratio。有看过之前面经，这个部分说的很模糊。说白了就是问，
在所有transaction with promotion中，transaction with promotion on first or last promotion day的比例是多少。我用了一个with 先吧transaction table和promotion table 做一个join得到有promotion的transaction table。然后在此表基础上用sum(case when )来统计在frist promotion day or last promotion day的个数 *1.0 然后再除以 COUNT(*)， 就是最后的ratio。
*/


SQL

               
我有印象的題目如下：               
1. find brands that have more than 3 products and the average price is higher than 2
2. find the rate of sales with promotion code
3. find the customers that buy products with brand XXX and OOO
4. find out how many different product classes our California customers have purchased from?
               
他有四個table (products, sales, stores, customers)，互相之間有foreignkey
products: product_id, brand_name, class, price, 
sales: product_id, store_id, transaction_date, customer_id, 
stores: store_id, store_type, country, product_id, customer_id, store_sales, promotion_id, transaction_date
customers: customer_id, gender, register_date, education 
               
               
'''
https://4.bp.blogspot.com/-_HsHikmChBI/VmQGJjLKgyI/AAAAAAAAEPw/JaLnV0bsbEo/s1600/sql%2Bjoins%2Bguide%2Band%2Bsyntax.jpg
'''

               
1. select 
               brand_name as "brand", 
               count(distinct product_id) "product_num", 
               ave(price) as "ave_price",
from products
group by 1
HAVING count(distinct product_id)>3 and ave(price)>2

2.  rate = sales with promo / total sales    
select 
        Round(ifnull(sum(case when s2.promotion_id is NUll 0 else 1 end)/sum(*),0),2) as "promotion_rate"
from 
        sales s1
        left join stores s2 on 
               s1.product_id = s2.product_id 
               and s1.store_id = s2.store_id 
               and s1.customer_id = s2.customer_id 
               and s1.transaction_date = s2.transaction_date

3. select 
               distinct(c.customers) 
   from customers c
   left join sales s1 on c.customer_id = s1.customer_id
   left join products p on s1.product_id = p.product_id
   where p.brand_name in ("B1", "B2")
               
4. 

