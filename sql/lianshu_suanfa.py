#算法一：蠡口 壹貳伍，125 验证回文字符串；
#算法二：n nearest point. SQL 题在 codepad 里跑出来正确答案就行，算法的话需要 go through几个 test case, 说说时间空间复杂度。
#题目一：蠡口 貳捌叁，要求写操作次数最少，
#题目二：深度拷贝一个图，图的结构自己定义，我用的是邻接矩阵定义。
#题目一： 蠡口 貳柒叁，
#题目二 贰柒柒，找名人的变种，不一样的地方是用string 表示每个人，follow up 是如果有多个名人，该怎么处理，具体细节有点忘。
#系统设计，设计 Facebook message，题目要求很简单，需求是A, B 两个人可以互相发消息，我问了日活用户，
#然后分析 QPS，存储等；然后设计数据库表，画系统流程图。
#然后 go through 整个流程，问如何加 load balancer, 如何加 cache，以及如何 scale。



#第二部分是算法题，也是一题接着一题，一题比一题难。。第一题是求List<String> words 长度的平均值，easy难度。
#第二题是确定一个ip address是不是valid的，也不是很难。。
#第三题是个图题，应该要dfs，但是时间已经用完了

'''
https://www.1point3acres.com/bbs/thread-447445-2-1.html
我来回答下，大致是给一个list of list表示两个node之间有朋友关系 然后统计每个node有多少朋友
input: [[A,B], [B,C], [A,C], [B,D], [E]]
output: {A:2, B:3, C:2, D:1, E:0}
我当时就loop了一遍然后加和，没时间太考虑更好的解法，
不过倒是一遍run就pass了。他们应该更考虑速度和能不能pass test，算法倒不是很重要'''
'''


'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=570831&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
Python部分很简单：
SQL：
1. 有fat_flag 和 另外一个flag的products，总之就是join两个表A和B 然后on的时候除了id, 再加上对与B表的两个flag的限制条件
2. 选出single media的products（还是什么其他的table，不是重点），point在single media：这个column有不同的值，e.g. SEO  |   SEO, Ads, website | Ads, website。 single media就是用like 语句来筛选一下就好
3. promotion ratio。有看过之前面经，这个部分说的很模糊。说白了就是问，在所有transaction with promotion中，transaction with promotion on first or last promotion day的比例是多少。我用了一个with 先吧transaction table和promotion table 做一个join得到有promotion的transaction table。然后在此表基础上用sum(case when )来统计在frist promotion day or last promotion day的个数 *1.0 然后再除以 COUNT(*)， 就是最后的ratio。
#'''
a = [1, 2, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]
b = [None, 2, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]
c = [None, None, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]

1. 给一个数字列表且里面有None，重新输出一遍把None位置的数用前面存在的数代替。a = [1, None, 2, None, None, 5, Ne]
def fill_none(a):
    for i, j in enumerate(a):
        if j is None:
            if i == 0:
                a[0] = next(item for item in a if item is not None)
            else:
                a[i] = a[i-1]
    return a

2. 给一个数字列表且某些数字重复，给出每个数字还需要加进多少个才能使得列表里每个数字都一样多。
nums = [1, 3, 4, 1, 7, 8, 3 , 2, 4, 5, 7, 2, 3, 5, 6, 4, 2, 8, 5]
def duplicated_nums(alist):
    max_dup = 0
    dup_rec = {}
    for ix, num in enumerate(alist):
        if num not in dup_rec:
            dup_rec[num] = 1
        else:
            dup_rec[num] += 1
        max_dup = max(max_dup, dup_rec[num])
    print("max:{}".format(max_dup))
    for key in dup_rec:
        print("num {}, current - {}, need - {}".format(key, dup_rec[key], max_dup - dup_rec[key]))
duplicated_nums(nums)


3. Average word length of a list of words。注意对每个word做.strip()
def ave_word_len(alist):
    total = 0
    for i in alist:
        i = i.replace(" ", "")
        total += len(i)
    return total/len(alist)

4. 给两个包含数字的列表，求两个列表里不重复的数字，不用在意输出顺序。
def diff_two_list(alist, blist):
    a = list(set(alist))
    b = list(set(blist))
    union = list(set(a + b))
    return [i for i in a if i not in union] + [i for i in b if i not in union]
    #list((set(a).union(set(b))).difference(set(a).intersection(set(b))))

Coding
a = (1, 0, 0, 2, 0, 0, 5)
b = (0, 0, 1, 3, 0, 1, 4)
dot product = 1*0+ 0*0 +... + 5*4 = 26
def dot_product(a, b):  
    if len(a)==len(b):
        sum = 0;
        for i, j in zip(a,b):
            sum += (a * b)
        return sum
    else:
        return "error message"



1.一个input String， 一个input Character，问你character在string里面出现了几次，恶心的是java input 他两个都给的string， 自己要转换下，然后注意null的corner case
def char_in_string(s, ch):
    count = 0
    for i in s:
        if i == ch:
            count +=1
    return count 



2.一个数组，把所有null换成前一个数字，关键是他给的input是Integer[],不是list，又debug 了半天。
def replace_null(list_num):
    for ix, num in enumerate(list_num):
        if not num and ix != 0:
            list_num[ix] = list_num[ix-1]
    return list_num



3.两个string， 求一个string[] 给出所有只出现在一个list中的word
def not_duplicated_word(alist, blist):
    return set(alist).union(set(blist)).difference(set(alist).intersection(set(blist)))

sql 就是那4道题 promotion， sale， product， product class， 多用case




Coding
一句话里平均单词长
def average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words)/len(words)

合法IP
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s): 
            try:
                return (0 <= int(s) <= 255) and str(int(s)) == s
            except: 
                return False
        
        
        def isIPv6(s):
            if len(s) > 4: return False
            try: 
                return int(s, 16) >= 0 and s[0]!= "-"
            except:
                return False
        
        
        if IP.count(".")==3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":")==7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"        
        return "Neither"

合法括号组合
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        table = {')':"(", "]": "[", "}":"{"}
        stack = []
        for i in s: 
            if i in table.values():
                stack.append(i)
            elif i in table.keys():
                if stack == [] or stack.pop() != table[i]:
                    return False
            else:
                return False
        return stack==[]
         
最短单词距离 - 243
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ix1, ix2 = len(words), len(words)
        minDistance = len(words)
        for ix, words in enumerate(words):
            if words[ix] == word1:
                ix1 = ix
                minDistance = min(minDistance, abs(ix1-ix2))
            elif words[ix] == word2:
                ix2 = ix
                minDistance = min(minDistance, abs(ix1-ix2))
        return minDistance
好朋友数量
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = 0
        seen = set()
        
        for person in range(len(M)):
            if person not in seen:
                self.dfs(person, M, seen)
                ans += 1
        return ans 
    
    def dfs(self, node, M, seen):
        for person, is_friend in enumerate(M[node]):
            if is_friend and person not in seen:
                seen.add(person)
                self.dfs(person, M, seen)
        
        

1. 一个string, 一个substr，计算substr出现的次数，不要用count函数
def count_substr(strA, substr):
    return strA.count(substr)

    count = 0 
    flag = True
    start = 0
    while flag:
        if substr in strA[start:]:
            count += 1
            start += len(substr)
        else:
            flag = False 
    return count


2. 一个list里面有None，把None用前一个代替，corner case里有第一个element就是none的，这时候就不用管，还是none就行
def replaceNull(aList):
    for ix, item in enumerate(aList):
        if not item and ix != 0:
            aList[ix] = aList[ix-1]
    return aList



#SQL，还是那个schema
指定平均价格和产品的品牌
有效促销比例
前三的产品
买了A和B的客户
买了不同产品数的客户数


