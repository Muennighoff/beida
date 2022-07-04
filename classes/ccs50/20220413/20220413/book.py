import sqlite3
dbConn=sqlite3.connect("lib.db",check_same_thread=False)
from flask import Flask,request,render_template #新增代码。装入Flask

#用户模块，userMag，用户管理
import userMag#载入用户管理模块

webApp=Flask(__name__) #新增代码

@webApp.route("/") #新增代码，对应执行root()函数
def root():
	cur=dbConn.execute("select count(*) from tblBook")
	tmp=cur.fetchall()
	bookAmount=tmp[0][0]
	return webApp.send_static_file("Register.html")

@webApp.route("/getData") #新增代码，对应执行root()函数
def getData():
	myQuery=request.args["svrQuery"]
	mySQL=f"select bookName from tblBook where bookName like '%{myQuery}%'"
	print(mySQL)
	cur=dbConn.execute(mySQL)
	send2Browser=""
	for rec in cur:
		send2Browser+=rec[0]+"###"
	print(send2Browser)
	return send2Browser[:-3]

@webApp.route("/getUserState",methods=('post',)) #获得用户状态
def getUserState():
	#获得浏览器端的传入数
	userName=request.form["userName"]
	#检测数据是否合规
	checkState=userMag.getUserNameState(userName)
	print(checkState)
	if checkState==False:
		return "0" #用户已经存在
	return "1" #用户不存在

@webApp.route("/userAdd",methods=('post',)) #用户注册
def userAdd():
	#获得浏览器端的传入数据

	userName=request.form["userName"]
	userPassword=request.form["userPWD"]
	#检测数据是否合规
	checkState=userMag.userCheck(userName,userPassword)
	if checkState==False:
		return "00"
	#检测用户名是否已经注册
	addState=userMag.userAdd(userName,userPassword)

	if addState==False:return '01'
	return "11"

if __name__=="__main__": #新增代码
	webApp.run(host="0.0.0.0",port=80,debug=True)
