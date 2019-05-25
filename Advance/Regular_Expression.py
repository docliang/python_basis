#coding=utf-8
#正则表达式练习
#导入re模块
import re

'''
匹配单个字符串
.	匹配任意1个字符（除了\n）
[]	匹配[]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符
'''
####################################################

#.用法总结：仅代表单个字符
# ret = re.match('.','Mac')
# if ret:
#     print(ret.group())
# else:
#     print('error')
#
# ret = re.match('t.o','t2o')
# if ret:
#     print(ret.group())
# else:
#     print('error')
#
# ret = re.match('t.o','ttp')
# if ret:
#     print(ret.group())
# else:
#     print('error')
#

####################################################
#[]用法总结：匹配括号内的字符,相当于有在范围内有符合标准的就行

# #小写匹配
# ret = re.match('h','hello,world')
# print(ret.group())
# #大写匹配
# ret = re.match('H','Hello,world')
# print(ret.group())
# #大小写通配
# ret = re.match('[hH]','Hello,world')
# print(ret.group())
#
# #匹配数字第一种写法，就是全写
# ret = re.match('[0123456789]','1hello')
# print(ret.group())
# #匹配数值第二种写法，简写范围
# ret = re.match('[0-9]hello','1hello')
# print(ret.group())
# #个性匹配,如下只能匹配到数字是(0-4)并上(6-8)这个范围的数字
# ret = re.match('[0-46-8]','4hello,world')
# print(ret.group())

####################################################
#\d 反斜杠 用法总结：就是专门用于匹配单个数字，无论数字多大

#常规匹配方式
# ret = re.match('嫦娥1号','嫦娥1号发射成功')
# print(ret.group())
# #使用\d开始匹配
# ret = re.match('嫦娥\d号','嫦娥8号发射成功')
# print(ret.group())

####################################################

'''
匹配多个字符
*	  匹配前一个字符出现0次或者无限次，即可有可无
+	  匹配前一个字符出现1次或者无限次，即至少有1次
?	  匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	  匹配前一个字符出现m次
{m,n} 匹配前一个字符出现从m到n次
'''

# *(❎) 需求分析：一串字符串第一个字母为大写字符，后面都是小写字母，后面的可有可无
#如MacBook 只能够显示出Mac
ret = re.match('[A-Z][a-z]*','Mook')
print(ret.group())

####################################################
# +