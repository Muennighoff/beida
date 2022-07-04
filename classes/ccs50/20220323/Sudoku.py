#数独
dataSudoku="700000000006750209004090000400002090080000020050800003000010500103048600000000001"
from flask import Flask,render_template #新增代码。装入Flask

webSudoku=Flask(__name__) #新增代码

@webSudoku.route("/") #新增代码，对应执行root()函数
def root():
    return webSudoku.send_static_file("sudoku.html")#发送静态页面

@webSudoku.route("/sudoku00") #新增代码，对应执行Sudoku()函数
def sudoku():
	tabSudoku="<table cellpadding='0' cellspacing='0' border='1'>"
	for i in range(0,9):
		tabSudoku+="<tr>"
		for j in range(0,9):
			cellNum=dataSudoku[i*9+j]
			zeroState=rightState=bottomState=False
			if cellNum=="0":
				cellNum=""
				zeroState=True

			if j%3==2 and j!=8:rightState=True
			if i%3==2 and i!=8:bottomState=True

			classValue=""
			if zeroState==True:classValue+=" zeroCell"
			if rightState==True:classValue+=" rightBolder"
			if bottomState==True:classValue+=" bottomBolder"
			classValue=classValue.strip() #清楚前后空格，不包括中间空格
			tdType="<td>"
			if len(classValue)!=0:tdType=f"<td class='{classValue}'>"
			tabSudoku+=f"{tdType}{cellNum}</td>"
		tabSudoku+="</tr>"
	tabSudoku+="</table>"
	return render_template("sudoku01.html",placeContent=tabSudoku) #必须是字符串类型
@webSudoku.route("/sudoku01") #新增代码，对应执行Sudoku()函数
def sudoku01():
	return render_template("JS_Basic04.html",placeContent=dataSudoku)

@webSudoku.route("/sudokuData") #新增代码，对应执行Sudoku()函数
def sudokuData():
	return dataSudoku+" from Flask Server!!!!"

if __name__=="__main__": #新增代码
	webSudoku.run(host="0.0.0.0",port=80,debug=True)
