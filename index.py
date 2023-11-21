from flask import Flask, render_template
import sqlite3 

app = Flask('__name__') 

@app.route('/')
def index():
	conn = sqlite3.connect('test.db')
	cur = conn.cursor()
	cur.execute('select * from terbaru')

	data = cur.fetchall()
	return render_template('index.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)