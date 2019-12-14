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
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=570831&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D13%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D2%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
Python部分很简单：
1. 给一个数字列表且里面有None，重新输出一遍把None位置的数用前面存在的数代替。a = [1, None, 2, None, None, 5, Ne]
2. 给一个数字列表且某些数字重复，给出每个数字还需要加进多少个才能使得列表里每个数字都一样多。
nums = [1, 3, 4, 1, 7, 8, 3 , 2, 4, 5, 7, 2, 3, 5, 6, 4, 2, 8, 5]
3. Average word length of a list of words。注意对每个word做.strip()
4. 给两个包含数字的列表，求两个列表里不重复的数字，不用在意输出顺序。list((set(a).union(set(b))).difference(set(a).intersection(set(b))))
'''
a = [1, 2, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]
b = [None, 2, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]
c = [None, None, None, 4, 5, None, 5, 4, None, 7, None, None, None, None]

def fill_none(a):
    for i, j in enumerate(a):
        if j is None:
            if i == 0:
                a[0] = next(item for item in a if item is not None)
            else:
                a[i] = a[i-1]
    return a


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



#Average word length of a list of words
def ave_word_len(alist):
    total = 0
    for i in alist:
        i = i.replace(" ", "")
        total += len(i)
    return total/len(alist)

#给两个包含数字的列表，求两个列表里不重复的数字，不用在意输出顺序。
def diff_two_list(alist, blist):
    a = list(set(alist))
    b = list(set(blist))
    union = list(set(a + b))
    return [i for i in a if i not in union] + [i for i in b if i not in union]
    #list((set(a).union(set(b))).difference(set(a).intersection(set(b))))