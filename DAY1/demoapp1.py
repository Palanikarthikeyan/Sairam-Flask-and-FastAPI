import flask 

obj = flask.Flask(__name__)

@obj.route("/")
def f1():
	return "<h1><font color=blue>Welcome to Flask App</font></h1>"

@obj.route("/aboutus")
def f2():
	return "<h2>This is about us page</h2>"

@obj.route("/mypage")
def f3():
	return "<h3>This is mypage </h3>"

@obj.route("/mycity/<myvar>")
def f4(myvar):
	return f"<h2>My living City is {myvar}</h2>"

@obj.route("/mycode/<pin>")
def f5(pin):
	return f"<h2>Pin code: {pin}</h2>"



if __name__ == '__main__':
	obj.run(debug=True) 
