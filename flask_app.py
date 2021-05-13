from flask import Flask, render_template, request, url_for, redirect
import sqlite3

def db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a secret key for your own'

@app.route('/')
def index():
    conn = db_conn()
    posts = conn.execute('SELECT * FROM table_posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create_new_post', methods=('GET', 'POST'))
def create_new_post():
    if request.method == 'POST':
        content = request.form['content']

        conn = db_conn()
        conn.execute('INSERT INTO table_posts (content) VALUES (?)', (content,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('create_new_post.html')