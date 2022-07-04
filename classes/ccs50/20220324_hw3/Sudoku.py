import os
import random
import string

import flask
from flask import Flask, render_template, request

dataSudoku = "123456789789123456456789123312645978978312645645978312231564897897231564564897201"
emptySudoku = "0" * len(dataSudoku)

webSudoku = Flask(__name__)

# Necessaary for use of flask.session
webSudoku.secret_key = ''.join(random.choice(string.printable) for _ in range(20))

webSudoku.config.update(
    TESTING=True,
    TEMPLATES_AUTO_RELOAD=True
)

def saveSudoku(sudokuString, outFile="Sudoku.data"):
	with open(f"{outFile}", "a") as f:
		f.write(sudokuString)
		f.write("\n")

def getSudoku(outFile="Sudoku.data"):
	if not os.path.exists(outFile): return False
	with open(f"{outFile}", "r") as f:
		sudokuLines = f.read().splitlines()
		sudokuString = random.choice(sudokuLines)
	return sudokuString

def createSudokuHTML(sudokuString):
	tabSudoku="<table cellpadding='0' cellspacing='0' border='1' name='table'>"
	isComplete = True
	for i in range(0,9):
		tabSudoku+="<tr>"
		for j in range(0,9):
			cell_idx = i*9+j
			cellNum = sudokuString[cell_idx]
			rightState = bottomState = False
			if cellNum=="0":
				cellNum=""
				isComplete = False

			if j%3==2 and j!=8:
				rightState=True
			if i%3==2 and i!=8:
				bottomState=True

			tdClassValue = inpClassValue = ""

			inpClassValue += "inputCellDefault"

			if (notInRow(sudokuString, i) is False) \
			or (notInCol(sudokuString, j) is False) \
			or (notInBox(sudokuString, i, j) is False): 
				inpClassValue += " inputCellRed"
				isComplete = False

			if rightState == True:
				tdClassValue += " rightBolder"
			if bottomState == True:
				tdClassValue += " bottomBolder"

			tdClassValue = tdClassValue.strip() #清楚前后空格，不包括中间空格
			tdType="<td>"
			if len(tdClassValue)!=0:tdType=f"<td class='{tdClassValue}'>"
			tabSudoku += f"{tdType}"#{cellNum}
			# Make readonly if already contains a number
			if cellNum:
				tabSudoku += f'<input type="text" class="{inpClassValue}" name="{cell_idx}" readonly="readonly" value="{cellNum}"/>'
			# Only allow a single digit from 1 - 9 
			# pattern will restrict submitting a creation with e.g. 00000
			# restrictKeys will restrict inputting any non numbers
			else:
				tabSudoku += f'<input type="text" onKeyDown="restrictKeys()" class="{inpClassValue}" name="{cell_idx}" pattern="[1-9]" value="{cellNum}"/>'

			tabSudoku += "</td>"
		tabSudoku += "</tr>"
	tabSudoku += "</table>"
	return tabSudoku, isComplete

@webSudoku.route("/") #新增代码，对应执行root()函数
def root():
	# 发送静态页面
	# May require disabling browser cache to show the correct one
	# Developer console > Network > Disable cache
	if getSudoku() is False:
		return webSudoku.send_static_file("sudokuHomeCreateOnly.html")
	else:
		return webSudoku.send_static_file("sudokuHome.html")

@webSudoku.route("/sudokuCreate", methods = ["GET", "POST"]) #新增代码，对应执行Sudoku()函数
def sudokuCreate():
	if request.method == "POST":
		newSudoku = list(emptySudoku)
		for idx, _ in enumerate(emptySudoku):
			val = request.form.get(f"{idx}")
			# Leave as empty / 0 if not filled
			if val:
				newSudoku[idx] = val
		newSudoku = ''.join(newSudoku)
		saveSudoku(newSudoku)

	# Do not act on isComplete here, as we are creating, not playing; Also this is always False anyways, as our Sudoku is empty
	tabSudoku, isComplete = createSudokuHTML(emptySudoku)

	return render_template("sudokuCreate.html", placeContent=tabSudoku) #必须是字符串类型


def notInRow(sudokuString, row):
	"""
	Checks whether there is any
	duplicate in current row or not
	"""
	# Set to store characters seen so far.
	st = set()

	for i in range(0, 9):
		# If already encountered before,
		# return false
		if sudokuString[(row * 9) + i] in st:
			return False

		# If it is not an empty cell, insert value
		# at the current cell in the set
		if sudokuString[(row * 9) + i] != "0":
			st.add(sudokuString[(row * 9) + i])
	
	return True

def notInCol(sudokuString, col=0):
	"""
	Checks whether there is any
	duplicate in current column or not.
	"""
	st = set()
	
	for i in range(0, 9):

		# If already encountered before,
		# return false
		if sudokuString[col + (i * 9)] in st:
			return False

		# If it is not an empty cell, insert
		# value at the current cell in the set
		if sudokuString[col + (i * 9)] != "0":
			st.add(sudokuString[col + (i * 9)])

	return True

def notInBox(sudokuString, row, col):
	"""
	Checks whether there is any duplicate
	in current 3x3 box or not.
	"""
	st = set()

	upperLeftRow = row - (row % 3)
	upperLeftCol = col - (col % 3)

	for row in range(0, 3):
		for col in range(0, 3):
			curr_idx = (upperLeftRow+row)*9+(upperLeftCol+col)
			curr = sudokuString[curr_idx]

			# If already encountered before,
			# return false
			if curr in st:
				return False

			# If it is not an empty cell,
			# insert value at current cell in set
			if curr != "0":
				st.add(curr)
	return True

@webSudoku.route("/sudokuPlay", methods = ["GET", "POST"])
def sudokuPlay():
	if request.method == "POST":
		cells = request.json.get("cells")
		sudokuString = "".join([x if x else "0" for x in cells[:len(emptySudoku)]])
		tabSudoku = ""
		# Store the new string and then reroute to GET in javscript
		# https://stackoverflow.com/questions/54733662/how-to-send-html-data-to-flask-without-form
		flask.session['sudokuString'] = sudokuString
		# Unfortunately, when using Ajax / Fetch & flask render_template, it does not update the page
		# We can get the template as a json like below, but I didn't figure out how to modify the entire DOM based on that JSON
		# return flask.jsonify({'html':render_template("sudokuPlay.html", placeContent=tabSudoku)})
	else:
		# If data was somehow deleted / user somehow got here, redirect to root
		if getSudoku() is False:
			return flask.redirect(flask.url_for('root'))
		tabSudoku, isComplete = createSudokuHTML(getSudoku())
		if isComplete:
			return flask.redirect(flask.url_for('sudokuPlayWin'))
	return render_template("sudokuPlay.html", placeContent=tabSudoku)

@webSudoku.route("/sudokuPlayUpdate", methods = ["GET"])
def sudokuPlayUpdate():
	tabSudoku, isComplete = createSudokuHTML(flask.session['sudokuString'])
	if isComplete:
		return flask.redirect(flask.url_for('sudokuPlayWin'))
	return flask.render_template('sudokuPlay.html', placeContent=tabSudoku)

@webSudoku.route("/sudokuPlayWin", methods = ["GET"])
def sudokuPlayWin():
	return flask.render_template('sudokuWin.html')

if __name__=="__main__":
	webSudoku.run(host="0.0.0.0", port=80, debug=True)
