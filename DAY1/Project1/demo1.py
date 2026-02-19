from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def f1():
	return render_template('display.html')

@app.route("/mygoogle")
def f2():
	return render_template('mysearch.html')

@app.route("/page1")
def f3():
	return redirect(url_for('f2'))

@app.route("/page2")
def f4():
	return render_template("view.html")

@app.route("/dept/<myvar>")
def f5(myvar):
	return render_template('dept.html',t_dept = myvar)

@app.route("/page3")
def f6():
	my_dept = 'Devops'
	return redirect(url_for('f5',myvar = my_dept))

if __name__ == '__main__':
	app.run(debug=True)

