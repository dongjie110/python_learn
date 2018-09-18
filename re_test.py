import re

"""
\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法）
re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为
"""


# 首字母缩写词扩充
"""
具体示例
FEMA   Federal Emergency Management Agency
IRA    Irish Republican Army
DUP    Democratic Unionist Party
FDA    Food and Drug Administration
OLC    Office of Legal Counsel
分析
缩写词  FEMA
扩展为  F*** E*** M*** A***
规律  大写字母+小写字母（一个或者多个）+空格
规律优化  大写字母+小写字母（一个或者多个）+空格+[小写（一个或者多个)+空格]（0个或1个）
"""

def expand_abbr(sen, abbr):
    lenabbr = len(abbr)
    ma = ''
    for i in range(0, lenabbr-1):
        ma += abbr[i] + '[a-z]+' + ' ' + '([a-z]+ )?'
    ma += abbr[lenabbr-1] + "[a-z]+"
    ma = ma.strip(' ')
    print('ma', ma)
    p = re.search(ma, sen)
    if p:
        return p.group()
    else:
        return ''

# print(expand_abbr("Food and Drug Administration", 'FDA'))
# print(expand_abbr("Federal Emergency Management Agency", 'FEMA'))


# 去掉数字中的逗号
"""
在处理自然语言时123,000,000如果以标点符号分割，就会出现问题，好好的一个数字就被逗号肢解了，因此可以先下手把数字处理干净（逗号去掉）。
分析  *,****,*
规则  \d,\d
"""
def get_digit(s):
    while True:
        mm = re.search('\d,\d', s)
        if mm:
            m = mm.group()
            s = s.replace(m, m.replace(",", ""))
            print(s)
        else:
            break
    print(s)

# get_digit("abc,123,456,789,mnp")


# 邮箱正则表达式
"""
someone@gmail.com
jeff.someone@gmail.com
<Charles Bird> bird@google.org
分析
<字母+[字母空格](1个或者多个)>(0个或者一个)+空格+字母或者数字（一个或者多个）+ @ +字母（一个或者多个)+.+com或者org
规律  ^(<\w[\w\s]+>\s)?(\w+[\w+.]*@\w+.(com|org)$)
"""
p = re.compile(r"^(<\w[\w\s]+>\s)?(\w+[\w+.]*@\w+.(com|org)$)")
m1 = p.match('someone@gmail.com')
m2 = p.match('jeff.someone@gmail.com')
m3 = p.match('<Charles Bird> bird@google.org')
print(m1, m2, m3)


# 电话号码匹配
"""
(021)88776543   010-55667890 02584453362  0571 66345673
分析
(0+数字{2到3位})（可有可无）或者数字0+数字（2到3位）+[- ](可有可无)+数字（7到8位）
规律  \(0\d{2,3}\)?\d{7,8}$|0\d{2,3}[- ]?\d{7,8}$
"""
p = re.compile(r"^\(0\d{2,3}\)\d{7,8}$|0\d{2,3}[- ]?\d{7,8}$")
m1 = p.match('(021)88776543')
m2 = p.match('010-55667890')
m3 = p.match('02584453362')
m4 = p.match('0571 66345673')
m4 = p.match('0571 66345673')
print(m1, m2, m3, m4)
text = "(021)88776543 010-55667890 02584533622 057184720483 837922740"
m = re.findall(r"\(0\d{2,3}\)\d{7,8}|0\d{2,3}[- ]?\d{7,8}|\d{7,8}", text)
print(m)


# 网页url正则
from urllib import request
url = "http://www.csdn.net/"
s = request.urlopen(url).read().decode('utf-8')
urls = re.findall(r"<a.*?href=.*?<\/a>", s, re.I)
for i in urls:
    print(i)
links=re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", s)
for i in links:
    print(i)


# 密码验证
# 至少8位字符，至少一个字母和一个数字
"""
asd2324fdder343
分析
字母（一个或者多个）数字（一个或者多个）（至少8位）
规律  ^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$
"""
p = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
m1 = p.match('asd2324fdder343')

# 至少8位，至少一个大写，至少一个小写，至少一个数字
"""
Aasd2324fdder343
分析
大写字母（一个或者多个）小写字母（一个或者多个）数字（一个或者多个）（至少8位）
规律  ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$
"""
p = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$")
m2 = p.match('Aasd2324fdder343')

# 至少8位，至少一个大写，至少一个小写，至少一个数字，至少一个特殊字符
"""
Aasd2324fdder343&
分析
大写字母（一个或者多个）小写字母（一个或者多个）数字（一个或者多个）特殊字符（一个或者多个）（至少8位）
规律  ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$
"""
p = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$")
m3 = p.match('Aasd2324fdder343&')