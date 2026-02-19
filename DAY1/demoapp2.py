from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def f1():
	return "<h1>Welcome to Flask App</h1>"

@app.route("/aboutus")
def f2():
	return "<h2>This is About Us Web Page</h2>"

@app.route("/display")
def f3():
	return "<h3>This is customer records</h3>"

@app.route("/mycity/<myvar>")
def f5(myvar):
	return f"<h2>My living City is {myvar}</h2>"

@app.route("/mypage1")
def f4():
	return redirect(url_for('f3'))

@app.route("/mypage2")
def f6():
	return redirect(url_for('f5',myvar="Pune"))

@app.route("/sales")
def f7():
	return "<h1>Requested dept is sales dept</h1>"

@app.route("/prod")
def f8():
	return "<h1>Requested dept is production dept total emp's are:120</h1>"

@app.route("/other")
def f9():
	return "<h1><font color=red>Sorry your requested dept is not found</font></h1>"

@app.route("/dept/<dept_var>")
def f10(dept_var):
	if(dept_var == 'sales'):
		return redirect(url_for('f7'))
	elif(dept_var == 'prod'):
		return redirect(url_for('f8'))
	else:
		return redirect(url_for('f9'))




if __name__ == '__main__':
	app.run(debug=True)

