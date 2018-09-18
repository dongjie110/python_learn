import time
from datetime import datetime, timedelta
from isoweek import Week
import calendar

# 获取当前时间str
now_s = time.strftime('%Y-%m-%d %H:%M:%S')
print(now_s)

# datetime -> string
now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str)


# string -> datetime
t_str = '2018-01-03 14:51:23'
d = datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
print(d)


# 日期加减
# 构造方法 datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 相差天数
now = datetime.now()
d = datetime.strptime('2018-01-01 14:51:23', '%Y-%m-%d %H:%M:%S')
delta = (now - d).days
print(delta)

# 计算n天后的时间
now = datetime.now()
n_days = now + timedelta(days=3)
print(n_days)


# 获取当前周，月，季度，年，并获取其日期段
now = datetime.now()
# 周，两种方式
w = int(time.strftime("%W"))
w = datetime.now().isocalendar()[1]
w_range = (Week(now.year, w).monday().strftime('%Y-%m-%d'), Week(now.year, w).sunday().strftime('%Y-%m-%d'))
# 月
m = datetime.now().month
m_range = (datetime(now.year, m, 1).strftime('%Y-%m-%d'), datetime(now.year, m, calendar.monthrange(now.year, m)[1]).strftime('%Y-%m-%d'))
# 季度
q = int(datetime.now().month + 2) // 3
quarter_time = {
    1: [datetime(now.year, 1, 1), datetime(now.year, 3, 31)],
    2: [datetime(now.year, 4, 1), datetime(now.year, 6, 30)],
    3: [datetime(now.year, 7, 1), datetime(now.year, 9, 30)],
    4: [datetime(now.year, 10, 1), datetime(now.year, 12, 30)]}
q_range = (quarter_time.get(q)[0].strftime('%Y-%m-%d'), quarter_time.get(q)[1].strftime('%Y-%m-%d'))
# 年
y = datetime.now().year
y_range = (datetime(y, 1, 1).strftime('%Y-%m-%d'), datetime(y, 12, 31).strftime('%Y-%m-%d'))
print(w, w_range, m, m_range, q, q_range, y, y_range)


# 获取当前星期几，四种方式
now = datetime.now()
d1 = now.weekday()  # 返回0-6，0代表周一
d2 = time.strftime("%w")  # 返回0-6，0代表周日
d3 = time.strftime("%A")
d4 = time.strftime("%a")
print(d1, d2, d3, d4)


# 根据当日获取下周日期范围
now = datetime.now()
dd = int(time.strftime('%w'))
if dd == 0:
    dd = 7
start_date = (now + timedelta(days=8-dd)).strftime("%Y-%m-%d")
stop_date = (now + timedelta(days=14-dd)).strftime("%Y-%m-%d")
print(start_date, stop_date)


# 本周当前日期获取前/后n周日期周范围
def get_n_week_range(n):
    now = datetime.now()
    dd = int(time.strftime('%w'))
    if dd == 0:
        dd = 7
    start_date = (now + timedelta(days=1+7*n-dd)).strftime("%Y-%m-%d")
    stop_date = (now + timedelta(days=7+7*n-dd)).strftime("%Y-%m-%d")
    print(start_date, stop_date)

# 本周
get_n_week_range(0)
# 下周
get_n_week_range(1)
# 上周
get_n_week_range(-1)
# 下下周
get_n_week_range(2)