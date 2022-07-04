from flask import Flask,request,render_template #新增代码。装入Flask

webApp=Flask(__name__) #新增代码

@webApp.route("/") #新增代码，对应执行root()函数
def root():
	return webApp.send_static_file("index.html")

if __name__=="__main__": #新增代码
	webApp.run(host="0.0.0.0",port=80,debug=True)
