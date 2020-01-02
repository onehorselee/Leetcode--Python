https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=570831&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
Python部分很简单：
SQL：
1. 有fat_flag 和 另外一个flag的products，总之就是join两个表A和B 然后on的时候除了id, 再加上对与B表的两个flag的限制条件
2. 选出single media的products（还是什么其他的table，不是重点），point在single media：这个column有不同的值，e.g. SEO  |   SEO, Ads, website | Ads, website。 single media就是用like 语句来筛选一下就好
3. promotion ratio。有看过之前面经，这个部分说的很模糊。说白了就是问，在所有transaction with promotion中，transaction with promotion on first or last promotion day的比例是多少。我用了一个with 先吧transaction table和promotion table 做一个join得到有promotion的transaction table。然后在此表基础上用sum(case when )来统计在frist promotion day or last promotion day的个数 *1.0 然后再除以 COUNT(*)， 就是最后的ratio。




https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=563796&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
DB题目：
这几个表，和以前说的有点像，但是我没看到过，谁看到过，麻烦指出哈
promotion， sales， product， promotion class四个表，后两个没用到。
这里对方的介绍和解释就 更南了！

1，得到某个column的值里面 只有一个值的 销售量前5。
2. 这个比较简单，记不清了，是一个比例，和promotion有关，就一个简单除法
3. 烦人的来了，又是一个比例，这次是 所有有promotion的trancation里 在promotion有效期第一天和最后一天的transaction占多少。
不是难，是对方的解释听不懂啊。。。 就是把sales表里的transaction日期 case when一下，除以全部就好。
也是就做完了3题，一共就给了50分钟，还迟到了几分钟。




https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=574779&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
SQL，还是那个schema
指定平均价格和产品的品牌
有效促销比例
前三的产品
买了A和B的客户
买了不同产品数的客户数




https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=565143&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
