from flask import Flask, render_template, request
import mysql.connector as sql
#import sqlite3 as db;

app = Flask(__name__)

con = sql.connect(host='lab3.cg06we0bxp1d.us-east-1.rds.amazonaws.com', user='admin', password='$Hanmuk8', database='shan');

#con = db.connect ('site1.db', check_same_thread=False);
c = con.cursor();

l = [10, 20, 30, 'abc', 40.5];
v1 = 20;
v2 = "name20"

@app.route('/index')
@app.route('/')
def index():
	return render_template ('blog/index.html', val = l, tit = "new title");

@app.route('/create_table')
def create_table():
	c.execute("create table sam (id int, name varchar(10))");
	con.commit();
	return render_template ('blog/index.html', val = l, tit = "new title");

@app.route('/insert_data')
def insert_data():
	c.execute("insert into sam values (%s, %s)",(v1,v2));
	con.commit();
	return render_template ('blog/index.html', val = l, tit = "new title");

@app.route('/select_table')
def select_table():
	c.execute("select * from sam");
	result = c.fetchall();
	return render_template ('blog/index.html', val = l, tit = "new title", result = result);

@app.route('/page2')
def page2():
	return render_template ('blog/page2.html');

@app.route('/calculate', methods = ['post', 'get'])
def calculate():
	a = int(request.form.get("t1"));
	b = int(request.form.get("t2"));
	c = a+b;
	return render_template ('blog/page2.html', ans = c);

if __name__ == "__main__":
	app.run (debug = True);
