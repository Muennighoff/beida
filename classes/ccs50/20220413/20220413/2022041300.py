import sqlite3 #使用SQLite的前提
 
#判断N是否为质数---开始
def isPrime(N):
    if N<=1:return "否"
    if N==2:return "是"
    for i in range(2,N):
        if N%i==0:return "否"
    return "是"
#判断N是否为质数---结束
 
dbConn=sqlite3.connect(":memory:") #创建内存数据库
dbConn.execute("create table tabPrime (intNum,isPrime)") #用来保存一个数是否质数
 
print(dbConn.execute("select * from tabPrime").fetchone())#输出：None
 
dbConn.execute("BEGIN") #亦可将BEGIN改为BEGIN TRANSACTION
for i in range(1,10000):
    dbConn.execute(f"insert into tabPrime(intNum,isPrime) values({i},'{isPrime(i)}')")
print(dbConn.execute("select * from tabPrime where intNum in (1,5,7,13)").fetchall()) #输出：(1, '否')
 
dbConn.commit() #回滚
print(dbConn.execute("select * from tabPrime where intNum in (1,5,7,13)").fetchall()) #输出：None
 
dbConn.close()
 
#eof