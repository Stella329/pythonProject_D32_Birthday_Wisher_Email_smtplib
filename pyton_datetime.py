import datetime as dt

# TAP INTO CURRENT DATETIME

now = dt.datetime.now() ##obj
## dt.datetime() == an obj.
## dt.datetime.now() : 秒后过于精确i.e. 2024-04-26 20:44:19.168236
## now_type: <'datetime.datetime'> --> obj
year = now.year ##atribute; type: int
day_of_week = now.weekday() ##method; 从0开始（星期一）


#CREATE YOUR OWN DATETIME OBJ

date_of_birth = dt.datetime(year =1997, month=3, day=29, hour=13)
## output: 1997-03-29 13:00:00



