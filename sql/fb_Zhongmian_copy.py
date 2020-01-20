'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=462208&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
2018-12-2
找工作终于告一段落了。非常谢谢地里的所有人。现在回馈地里。大家多练习多mock多刷题，你会感谢这么努力的自己的。艰难的岁月终会过去。一切都会好的。因为打算接了这个offer了，所以不能透露具体的题目信息。不过地里的面经已经都说的差不多了。3轮 full stack + 1轮BQ
每轮的full stack都从一个具体的产品出发。例如DAU，update photo，uber。分析用什么metrics衡量产品，如果一些数据drop了，
可能是什么原因造成的。之后开始写sql和python。
题目都是这个套路。真的是取决于面试官和面试官的心情决定问什么问题。
我碰到的一个面试官问的问题超级发散。感觉不好准备。就靠当时沟通了。其它的几轮还挺常规的。
coding部分lc easy难度。主要考点就是update dict。不用太担心。sql要求还挺高的。
当时有一轮还有两个sql没写出来。幸运的过了。self-join, outer join，aggre都是考点。
没有不让写sub query。也没有让写window function。
重点是product sense，我觉得也是bar最高的一部分。
lean analysis那本书很经典的，地里也很多人提到过我就不说了。
还想给大家推荐一个网站。https://stellarpeers.com/ 里面有一些分析的文章很有用！！！重点推荐。
还可以和别人约mock。这块重点就是多mock。自己内心有答案真的不代表能表达清楚。我当时基本每块都mock了几遍。问不同人的意见。也真心感谢帮助我的小伙伴们。分析问题break down的时候也多和面试官沟通。
BQ问题都很常规，conflict，challenge什么的肯定要准备的。还有一个对fb产品的建议。
'''

'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=459745&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
2018-11-20
昂赛当天：
第一轮是behavior，印度小姐姐。自己刚进去就面behavior，感觉很紧张，一些情形说得不清楚，小姐姐问了我好几处，让我clarify。
感觉这一轮是面得最不好的，之前准备都是把这些问题的答案放在心里过一遍，和跟别人说清楚确实不太一样。
然后自己resume里面有一两段经历准备得不是很充分，碰巧又被她拿出来一直问 
（比如她问我一段big data project经历里面有什么和队友不合的事情， 我之前准备这个问题的时候是用另一段经历来回答，
这一段就没有准备到）。还有最后一个问题，是对FB的产品有什么建议，哪些觉得可以改进的。
这个我之前完全没有准备，犹豫了一会，她说时间也到了，就这样吧
第二轮是project sense，一个中年白人大叔，一开始问一些data visualization的东西，
然后让我找一个评价steps in funnel里面的metric，他期待的答案是conversion time，我愣是没说上这个，
然后他就直接告诉我了，然后基于这个metric，让我写了一些SQL和Python (Python是用来把stream改成real time的)。 
后面倒是写得很顺利，唯一不足的可能就是变量定义得不是很清楚。
我用string.split 变成一个list，然后后面直接用 list[0], list[1], list[2], list[3] 他检查我code的时候，
在这种变量分别代表什么的时候有点晕，跟他解释了才清楚。
中间休息，我的HR来问问我情况，我说behavior面的不好，她一直安慰我，说后面面得好就行了，
也给了我一些有用的面试经验。然后一个白人小哥带我去吃午饭，他很厉害，是个team的manager了，
和我聊了很多FB文化，职业发展的东西，我也问了一些他们正在做的项目。这个部分不算分，所以就随便聊聊了。
第三轮是 SQL 和 算法， 一个印度小姐姐。大概就是给一些背景材料，让估计Daily active user的各个方面，
比如哪些是连续用户，哪些是返回用户，哪些假设已经churn 了，然后用SQL 来计算每天的这些数据。她一步步带着我写，
虽然最后的SQL还挺复杂的，但是她一步步带着我，循序渐进，所以也并不难。最后也是把这些东西用Python来写一下，
处理一些dictionary, nested list, 几个嵌套循环就出来了。感觉她也很满意
第四轮是 data modeling， 一个白人小哥。我感觉我就是刚来的时候很紧张，然后之后越来越好，最后一轮的时候已经完全放松了。
这一轮让设计一个类似于Uber的 FB ride。 主要是设计后台数据库的schema，我用的是star schema，
一个大的fact table连一些具体的dimentional table。感觉非常顺利，小哥人也很nice。
然后基于这个设计，写了一些SQL，也是他带着我循序渐进，写得也非常顺利，沟通也很好。
最后写出来的SQL还挺复杂的，用了不少 电面考到的 having + aggregation function的 方法。
自己中间稍微有几个typo，小哥一指出我就发现了。最后还有一点时间，用来问他几个问他，
以及我之前一个关于推荐系统的project（因为小哥就是推荐系统组的）。 最后walk out。
总体感觉technical部分挺简单的，SQL熟练了就行了。 product sense还是要多看，对于new grad这部分也不太好准备。
面完感觉整体应该过的概率比较大，主要担心就在behavior上 （因为听说FB的DE还是很重视 communication的），
product sense也就conversion time没有答出来，别的也还好，后两轮感觉很不错。
结果没想打今天还是受到了拒信。可能面得简单，所以大家表现得都不错吧。正在向 HR 要feedback中。
楼主12月就毕业了，感觉现在非常慌，还没有一份offer。祝各位一切顺利，早日上岸吧
'''

'''
2018-11-15
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=458089&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
onsite: sql + python (挂在python)， 地里的面经稍微改变了下而已
挂的原因：听的以为是原题，太激动， 以为稳了。。。其实有一些改变（比如3 steps变成5 steps， 加大了一点难度而已）
总的来说，题都是他们平常遇到的问题，context of excercise could be a funnel analysis, how do you calculate average time bw steps，很intuitive！
稳稳地练好hackerrank的sql 以及 leetcode easy level 会是很好的starting point
锦上添花： product sense, （本来做product analyst所以没有特别准备这一点），了解基本的kpis, steps in the funnel，描述有调理就行了
'''

'''
2018-10-8
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=448129&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
10/1, on site. 一轮data modeling, 两轮ETL, 一轮behavior. 
内容和他们发的prep material里一致. 
在此感谢地里大佬的分享http://www.1point3acres.com/bbs/thread-330947-1-1.html. 
尤其是case study的部分, 特别特别有帮助.
on site就没有直接考coding了, 但是会在case途中根据自己之前的设计问问题, 
类似于我们现在有这个table/data stream, 算这个metrics用SQL怎么写, 换成python怎么写.
10/5收到电话, 说HM不在没有开成会, 这周二一般会开会出结果告诉我. (和地里其他面他家的说法很一致......同一个HM吗......). 默默祈祷.
总结一下:
1. 一定要刷完tag原题里easy和medium的
2. SQL我也普通水平, 也没有考察太复杂的
3. 按照prep material, 学习地里大佬经验
'''

'''
Onsite一共五轮，每轮四十五分钟，一轮 SQL，两轮算法，一轮 behavior question，一轮 system design。、
第一轮：华人小哥，SQL 题，给一个 table叫做水果，里面存有橘子和苹果，连着问了很多问题，
都不太难，而且会给提示，面试官人特别好。
第二轮：烙印，算法题，题目一：蠡口 貳捌叁，和电面二题目一样，我也很懵逼，秒了。
题目二： 蠡口 貳壹壹，题目稍稍有一些不一样，但是思路是一样的，用trie，秒了。整个过程烙印一直在看手机，写完走一遍 test case 然后没问题，牌照走人。
午饭和 recruiter闲聊。
第三轮： 烙印，算法题，题目一： 蠡口 貳柒叁，
题目二 贰柒柒，找名人的变种，不一样的地方是用string 表示每个人，follow up 是如果有多个名人，
该怎么处理，具体细节有点忘。
第四轮： 白人 manager，behavior question，大概问题有：最成功的 project 是什么？为什么觉得成功？
你觉得怎么样才算一个成功的 project？ 和上司有意见不一致的时候是怎么解决的，和同事有冲突的时候怎么办，
做过比较失败的 project 是什么，有没有什么比较后悔的事情，如果再给你一次机会，你应该怎么做？
这一轮的要点是自己要提前准备好故事，即使和上司没有过意见不一致的例子，也要自己准备一个，心里面排练好，
而且这轮回答问题要多准备几个 project，不要只用一两个 project 回答完所有问题，要多举例子，哪怕是学校的 project。
第五轮： 烙印，系统设计，设计 Facebook message，题目要求很简单，
需求是A, B 两个人可以互相发消息，我问了日活用户，然后分析 QPS，存储等；
然后设计数据库表，画系统流程图。然后 go through 整个流程，
问如何加 load balancer, 如何加 cache，以及如何 scale。
面试准备 tips：
算法和 SQL 就猛刷 leetcode，还有看面经；
behavior question自己编故事；
系统设计我看了某章的课程和这个课程 https://www.educative.io/collect ... Name=Design%20Gurus
FB 系统设计比较高频的几个题好像是：design POI， design instagram, design facebook messager, design news feed.
'''




'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478169&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3089%5D%5Bvalue%5D%5B3%5D%3D3%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
非死不可DE， 
onsite, 2019/1/18
Round 1: 华人男， 设计uber 
1）问了一些简单的 evaluation metrics. 
2) 建表。用了star shcema 没有异议。 
3）问了四个SQL 都秒过，比如平均驾驶时间， 累计驾驶过4h的司机， 只往返机场的乘客（这题用了两种办法都过，不过面试官提出另外一种leftjoin 的方法也很棒）
4）闲聊
Round 2：印度女， upload feature 那题。感觉非常不专业也不nice。
1）上来问了几个metrics， 似乎没有说中她心里的答案，女烙印就很push，不给思考时间各种连问，how！how！how！， 我几乎被堵到说不了话。 
2）接着给了一个upload表，也不说有没有duplicates， 遇到duplicate的要求是啥。于是我反问烙印，烙印一脸迷茫看着我说，你想怎么处理。我说取每个重复时间的最小值，烙印说好吧 （难道这不应该是面试官告诉我的题目要求么！！）。写完SQL，烙印说不知道对不对。我打算写第二种方法让她明白，不过她拒绝我写下来，大概口头说了下，拍照第一种方法，下一题。
3） coding：处理一个很大的stream，我说了我的思路，我打算用hashmap 和 array 的结构，烙印要求立即给一个best solution，不许用array。我当时懵了，讨论十分钟没有figure out。然后我一看时间来不及了，说我先写个普通解答再优化吧，烙印同意了。 写完各种解释让烙印搞懂，烙印说即使这样也不是最最优解。 我说不用array感觉很难，烙印好像觉得自己给的条件错了，她立马说，是不用hashmap， 然而只有几分钟，我大概说了一下。。。结束。(我内心挺无语的，为什么一上来给了我一个错的条件，最后又换掉)
Round 3：一个白人和烙印（还是中东， 远程看不清）问了各种BQ， 比方为啥来DE， 以后做啥。。等等。正常聊天，感觉不到好坏。
Round 4:  一个亚裔感觉是ABC， 很帅。哈哈哈。  言归正传，问了 各种new users， return users blabla 写SQL 秒过。中间有个小小的不算bug 的一行， 他觉得可以省略不写一样正确。
                 Coding ， 面经里各种rollup，楼主java 用的hashmap秒过
过了一周收到回复，说送去了hc，再过两天收到no-go， recruiter 给的feedback是technically perfect but product sense not that good。 楼主猜想第二轮女烙印 上来连问那里可能答的不满意吧，其他真的想不起来了。
挺遗憾也有点失落。感觉准备万全才去的。关于product sense，楼主现在是SDE，确实不知道怎么样才叫好，感觉都是开放问题，求指教。
'''




'''
2019-3-15
2 coding 1 behavior
以下内容需要积分高于 100 您已经可以浏览
1. intersection of two sorted arrays. follow up: if one of the arrays is extremely large.
藜蔻 奇溜
2.  3sum. follow O(n)
利口 尔雾散
3. likou 洱器霸
tough project and how to deal with it
3sum O(n) 没有想出来，面试官就说 never mind，然后就下一题了。
'''


'''
2019-8-7
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=541877&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3089%5D%5Bvalue%5D%5B3%5D%3D3%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
hr面很简单，主要是她在说，各种介绍，就问了三个问题，一个答案是join，一个是group之类的，最后一个是雪花型和星型的区别
技术面：
SQL: 经典的product的那四个表，地里就有
题目也是面经里的，一个是count同时买2 个商品的人，一个是count(case... when... ), 一个是求百分比
Python: 蠡口三舅舅
onsite 4轮：
一个表是项目，人，另一个表是人，工作年限。
第一个题目超简单忘了，
另一个count（case 。。。when。。。）选出只有年限小于1年的员工的项目有几个？
但比电面那题难问了个big data distribution的问题，蒙了，压根没准备
第二轮python：
一个是split list，一个merge list, 
最后一个是调用这两个function，写一个mergelist（非sorted）要求O（nlogn）
第三轮BQ: 校友，愉快的聊天
第四轮DATA MODELING: hm 不怎了我，自己在忙，写好了也没有follow question，
就说很好就没了，还问了怎么control data quality，很简单，自己觉得该答得都答了
跪的有点莫名其妙
'''



'''
https://www.1point3acres.com/bbs/thread-547398-1-1.html
FB面试总结FB 店面加昂赛，DE和SWE两个赛道同时搞。前后总共一个月时间。
先说DE
DE店面主要包括两方面的内容，SQL，coding。SQL有的题目还是比较tricky的。
但是如果熟手的话，也不难搞掂。基本概念包括主键，外键，规范，去规范，合并，
外合并，左合并，右合并，以及集合操作。

昂赛过程：
1 三哥manager视频面试。BQ。其中一题问给我一个你的数据助力产品开发的具体例子。
另外一题问我和老板有分歧的例子，还有最后结果
谁认怂。当然我认怂了。

2 欧白大叔。设计数据模型。给一个网络用户注册流程，数据埋线设计，metrics设计。
SQL求用户最花时间的是哪一步。

3 同胞陪吃午饭 各种真心点拨加吐槽。非常感谢。FB的文化是 movefast, 
open to feeback, talk about your project。

4 友好三哥 设计网约车平台。SQL找出只服务送机或者接机的司机数目。
这里大叔我用了一个新颖一点的方法让三哥质疑了好一阵。好险。

5 同胞小妹 问某款网上服务新版发行后发现metrics和dashboard异常，如何找出根问题。
然后问了一个SQL问题：某BBS统计用户登陆历史


数据模型为【用户名，登录时间】。每天都有一个数据分区。历史数据存档在总数据库。依一下规则将用户分类：新用户是今天登陆（当然也是今天注册）；回头用户是昨天没有登录今天登录；断续用户是昨天登录今天没有登录；潜水用户是昨天今天都没有登录。用一个SQL把所有用户分类统计。
接下来是coding。给一个JSON代表用户终端登录数据
users
{
‘userid1': {
   ‘android’: [0 1 1 1 0 0 1],
   ‘iphone’: [1 0 0 0 0 1 1],
},
'userid2': {
  ‘mac’: [0 1 0 1 0 0 1],
  'pc’: [0 1 0 1 0 0 1],
  ‘android’: [0 1 0 0 1 0 1]
}. From 1point 3acres bbs
...
}
每个用户可以有多种终端登录。其中整数数组长为7，表示一个星期每一天是否登录。
rollup
{
‘mobile’: [‘android’,’iphone’],
‘desktop’: [‘mac’, ‘pc’],-baidu 1point3acres
...
}

些一个UDF来rollup一个用户登录一星期的登录情况。用哈希集合或者比特集合都可。
总的感觉是FB把DE当成低端eng来用，要有产品经理的敏锐和商业运作头脑。
主要看重SQL和一些可视化报表和presentation能力。大家加油吧！

SWE 请见另帖


https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=556517&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3089%5D%5Bvalue%5D%5B3%5D%3D3%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
2010-10-4
据猎头说，上次昂赛一个面试官和同事意见不和。为慎重起见，决定加面一次。我还以为全程behavior呢。
可是全程技术面试！
第一题：给出YOY DAU 增长率 15%，YOY posting user 增长率 8%。分析数据背后的故事。
这题很刁钻。我就死马当活马医，心一咬，牙一横，开始从人口分布说起，又说到人口老化问题，
再说到产品feature发布，
最后在面试官提示下，说到用户使用终端从desktop到mobile，mobile 安卓和苹果之争的问题，等等。
其实这道题问的就是数据的dimension问题。

第二题：给出一个数据库table，有四个列：
userid int
timestamp datetime
action enum {"login", "send", "update"}
client enum {"android", "iOS", "desktop"}
问如何得到每天数据
DAU
send count
iOS send count
新用户
date
我根据以往的经验，就说根据上述数据，建立一个table，每天分区。
这两个table full outer join后这样的数据很容易得到。
第三题：给出一群metric table，share共同的列“date”，其他的列follow同样的结构，就是
- 有一个 dimension 列，每个table名字不一样
- 有一个或多个metric列，每个table名字不一样
以下内容需要积分高于 100 您已经可以浏览
如何写script产生一个query，把这群tables数据变换成如下格式并插入到warehouse数据库里？
date
dimension
dimension_value
metric
metric_value
面试官很善良地给hint。我各种配合。
最后的解是：用Python写脚本程序，用JSON传递数据库schema，用txt文件写template。
def query_gen(json, template):
     return ‘ union ‘.join([table_query_gen(table, template) for table in json.tables])
def table_query_gen(table, template):
     return ‘ union ‘.join([col_query_gen(table.name, col, table.dim, template) for col in table.metrics])
def col_query_gen(table, col, dim, template):
     return template.format(table=table, col=col, dim=dim, metric=col)
结论：数据工程师职位不好拿呀。需要product sense。面试时候套路挺多，挺独特的。祝各位好运！求加米
'''


System design: design uber
dispatch system 
constant hashing
load balancer 
web sockets  


'''
1x – Data Modeling problem (1 hour)
2x – ETL problems (1 hour each)
1x – Ownership discussion (30 minutes)
1x – Lunch (1 hour)


Data Modeling
You will brainstorm the data needs of a user product. Then you will design a data mart to support analytics use cases and write select SQL statements to produce specific results

ETL
You will solve a complex ETL (extract transform load) problem.
You will design source and target schemas and write SQL and procedural code to transform and load the data.

Ownership
Data Engineers need to take initiative in their role, 
so we will ask questions about your past experiences 
where you have been able to demonstrate this.

Lunch
Lunch with one of our Data Engineers, which will be your chance to 
ask all questions you have about what life is like as a Data Engineer at Facebook.

Additional Resources:
Here are some links that you might find helpful in preparing for the interview: 

Data Modeling
https://en.wikipedia.org/wiki/Data_model
https://en.wikipedia.org/wiki/Data_mart
https://en.wikipedia.org/wiki/Dimensional_modeling
https://en.wikipedia.org/wiki/Denormalization

SQL
SQL Tutorial 

Code - basic procedural concepts, Python, Java, or Scala (use the guide for the language you plan to use during the interview)
Python Guide 
Java Guide
Scala Guide

The Data Engineering team works very closely with various Product Analytics teams here at FB, thus familiarizing yourself with our current products can help you understand the company better. http://newsroom.fb.com/products/
 
This is not needed for preparation purposes but is good to view if you want more insight into the custom ETL that Facebook uses, Dataswarm: https://www.youtube.com/watch?v=M0VCbhfQ3HQ

Below are some recently posted external bios for Data Engineers from the team. These will help give you a better sense of what drives the Data Engineers within Facebook Analytics.

 

An inside look at Data Engineering at Facebook
https://fb.careers/DERohitBio
https://fb.careers/MichaelBBSB
https://fb.careers/ShawnaBSB
'''


Growth Data Engineering, Data Foundation, Product Metrics, Data Logging, Data Visualizations, Reporting, Hadoop, Presto, Spark, Python

Rahul pardeshi - DE five years: ETL 
sandeep kachru - product analytics mgr 
Dima Faradjev - Nothing
Mandy gerde - instagram mgr 


1st normal form: 
#remove duplicate data and break data at granular level

2nd normal form: 
#all column data should depend on full primary key and not part 

3rd normal form: 
#no column should depend on other columns

OLTP-

OLAP- 

