import sqlite3
dbConn=sqlite3.connect("lib.db",check_same_thread=False)

#获得用户状态，比如：判断用户是否已经注册
def getUserNameState(userName):
	sql=f"select * from tblNewUser where userName='{userName}'"
	print(sql)
	cur=dbConn.execute(sql)
	checkState=cur.fetchone()
	if checkState==None:return False
	return True#表明该用于已经存在

#用户名合规检测,此处仅检查密码长度是否合规
def userCheck(userName,userPWD):
	print("userCheck!00")
	if len(userPWD)<8:return False
	print("userCheck!01")
	checkState=getUserNameState(userName)
	print("userCheck!02")
	if checkState==True:return False
	print("userCheck!03")
	return True

#在用户名合规后，真实增加到数据
def userAdd(userName,userPassword):
	sql=f"insert into tblNewUser (userName,userPassword) values('{userName}','{userPassword}')"
	print(sql)
	try:
		cur=dbConn.execute(sql)
		dbConn.commit() #物理写入数据库
	except:
		return False #发生异常，则返回False

	return True#表明数据库存入成功

if __name__=="__main__": #新增代码
	userCheck("DXF")
	userAdd("DXF","02507")