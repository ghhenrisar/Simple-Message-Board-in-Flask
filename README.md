# Simple Message Board using Flask

![Semantic description of image](https://raw.githubusercontent.com/ghhenrisar/simple_msgboard/master/images/Monitor014400336.jpg)

If you want to find a entry point to learn web programming for a message board, this project will do. Flask is a tool for web developing. A preview of the message board is available [here](http://pahenrisar.pythonanywhere.com/). And the source code located [here](https://github.com/ghhenrisar/simple_msgboard).

## Preparation
For beginner of Python, I would suggest PyCharm as your development environment. You can get started [here](https://www.jetbrains.com/help/pycharm/quick-start-guide.html).
> PyCharm is a dedicated Python Integrated Development Environment (IDE) providing a wide range of essential tools for Python developers, tightly integrated to create a convenient environment for productive Python, web, and data science development.

Virtual environment is useful when you are learning or writing codes becuase each virtual environment is stand-alone such that other environment is not affected. [PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) can also support this.
> PyCharm makes it possible to use the virtualenv tool to create a project-specific isolated virtual environment. The main purpose of virtual environments is to manage settings and dependencies of a particular project regardless of other Python projects. virtualenv tool comes bundled with PyCharm, so the user doesn't need to install it.

In this project, we are going to use [Flask](https://palletsprojects.com/p/flask/).
> Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

Some basic knowledge of Python, SQL and HTML is required for this project but I will keep it as simple as I can.

### To install flask
Run the following command at Terminal (e.g. PyCharm Terminal):

`pip install flask`

### The structure of the directory
```
./simple_msgboard/
    |--database.db
    |--flask_app.py
    |--schema.sql
    |--templates/
        |--base.html
        |--create_new_post.html
        |--index.html
```


## Main flask application: flask_app
Create a new Python file `flask_app.py` and type the following code:

---

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

---

`Flask(__name__)`
> Flask is required to be imported so that Flask application can be initialized.

```python
@app.route('/')
def index():
    return render_template('index.html')
```

> `/index.html` will be returned when the root('/') of website is accessed.



## Test run of flask app
Create a HTML file `index.html` at the directory `./simple_msgboard/templates/`.
Then run the following command on Terminal (e.g. PyCharm Terminal). Note: each OS has its own command, please find the details at this [link](https://flask.palletsprojects.com/en/1.1.x/cli/).
```
set FLASK_APP=flask_app
flask run
```
The output should be something like below:
```
 * Serving Flask app "flask_app"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Now you can browse the web page of `http://127.0.0.1:5000/` and you should see a blank page.

## Base HTML template
We will create a HTML template `base.html` such that each HTML web page can inherit without repetition of the code.
Type the following code on `base.html`.

---

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title> {% block title %} {% endblock %} </title>

  </head>
  <body>
  <!-- Bootstrap Navigation Bar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <span class="navbar-brand">Simple Message Board</span>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/create_new_post">New Post</a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        {% block content %} {% endblock %}
    </div>

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

---

### Bootstrap 
Some basic of HTML on the above page can be found [here](https://www.w3schools.com/html/html_basic.asp).<br>
Bootstrap is utilized for better performance with different device, such as smartphone. You can learn more [here](https://getbootstrap.com/docs/5.0/getting-started/introduction/).

### Jinja
`{% block title %} {% endblock %}`
It is the delimiters of [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/). We will use these to interit the code later.

>There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:
<br>{% ... %} for Statements
<br>{{ ... }} for Expressions to print to the template output
<br>{# ... #} for Comments not included in the template output

### Create new post link
`<a class="nav-link" href="/create_new_post">New Post</a>`
is the link of the page to create a new post. We will explain this at the section `Link for Create New Post at Base HTML template` later.

### Preview
![Preview](https://raw.githubusercontent.com/ghhenrisar/simple_msgboard/master/images/3%20preview.png)

## Database Construction
In this project the database stores the messages and the time when the message submitted. SQL is often used for this purpose. Let's create `database.db` and `schema.sql` at the root directory of this project. [Sqlite](https://sqlite.org/index.html) is the library in this project for the communication between database and front end. 

Type the following code on `schema.sql`

---
```sql
DROP TABLE IF EXISTS table_posts;

CREATE TABLE table_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL
);
```
---

### DROP TABLE
We drop the table named `table_posts` if it already exists to ensure proper functionality.

### CREATE TABLE
Table `table_posts` is created with the following columns.
- `id`: index
- `time_stamp`: date and time when the message is submitted (automatically created)
- `content`: the submitted message

### Create table on terminal (e.g. PyCharm terminal)
Type the following code on the terminal: <br>
`sqlite3 database.db < schema.sql`

### Database connection with Flask
Please update the code on `flask_app.py` as below:

---
```python
from flask import Flask, render_template
import sqlite3

def db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return  conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = db_conn()
    posts = conn.execute('SELECT * FROM table_posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
```
---

`sqlite3` is imported for the following code:<br>
- `def db_conn()`: function to make connection with database<br>
- `posts = conn.execute('SELECT * FROM table_posts').fetchall()`: get all the data from `table_posts` and then pass the data to object `posts` when redirecting to `index.html`

## Home Page
Type the following code on `/templates/index.html`:

---
```html
{% extends 'base.html' %}

{% block title %}
    Simple Message Board
{% endblock %}

{% block content %}
    {% for post in posts %}
        <br>
        <div class="card">
            <div class="card-body">
                <p class="card-text"> {{ post['content'] }} </p>
                <span class="badge badge-secondary">{{ post['time_stamp'] }}</span>
            </div>
        </div>
    {% endfor %}
{% endblock %}
```
---

### Below is the implementation of Jinja
- `{% extends 'base.html' %}`: inherit base.html so there is no need to repeat the html scripts again
- `{% block title %} Simple Message Board {% endblock %}`: the block title is replaced by the string `Simple Message Board`
- `post['content'] and post['time_stamp']`: display the content and time stamp of each message by a for loop

## New Post Page
Update the code on `flask_app.py` as follows:

---
```python
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
```
---

`request, url_for, redirect` is imported for the following:
- `app.config['SECRET_KEY']`: for client-side sessions security
- `@app.route('/create_new_post', methods=('GET', 'POST'))`: a new route to `create_new_post.html` with data exchange between client and server side by GET and POST methods
- `content = request.form['content']`: pass the submitted message to the variable `content`
- `conn.execute('INSERT INTO table_posts (content) VALUES (?)', (content,))`: update database with the submitted message to the column `content`
- `return redirect(url_for('index'))`: redirect to `index.html` after updating the database

### Link for Create New Post at Base HTML template
`<a class="nav-link" href="/create_new_post">New Post</a>` is the link for `create_new_post.html` at `base.html` that we mentioned previously. You can find the following code on `base.html`:

---
```html
...        
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/create_new_post">New Post</a>
                </li>
            </ul>
        </div>
...
```
---

### Create New Post Page
Add the following code on `/template/create_new_post.html`:

---
```html
{% extends 'base.html' %}

{% block title %}
    New Post
{% endblock %}

{% block content %}
    <br>
    <form method="post">
        <div class="form-group">
            <label for="content">Create New Post</label>
            <textarea name="content" placeholder="Write a content..." class="form-control" id="content" rows="9" required>{{ request.form['content'] }}</textarea>
        </div>
        <button type="submit" class="btn btn-success">Submit</button>
    </form>
{% endblock %}
```
---

About the above code:
- Similar to `index.html`, `create_new_post.html` also inherit the code from `base.html`
- `New Post` is set to the block title 
- `<form method="post">`: the message will be sent to server when 'Submit' button is pressed

## Preview of This Finished Project
![Preview](https://raw.githubusercontent.com/ghhenrisar/simple_msgboard/master/images/8%20preview.png)

## Conclusion
This is a simple message board. You can try to add a function to allow formatting of the message (e.g. colour of the text) for improvement. And, as you can see, user cannot register and no log-in function. `Flask-Login` is one soulution for this. Add a link of sign-in at `base.html` for users to login and then post, edit or delete their messages. 

If you want to deploy this project to `pythonanywhere.com`, modification of WSGI configuration file at pythonanywhere control panel (on the "Web" tab) is required. And you have to change the settings below.

```
Source code:
/home/your_user_name/simple_msgboard/
Working directory:
/home/your_user_name/simple_msgboard/

Virtualenv:
Use a virtualenv to get different versions of flask, django etc from our default system ones. More info here. You need to Reload your web app to activate it; NB - will do nothing if the virtualenv does not exist.
/home/your_user_name/.virtualenvs/your_virtualenv_name/
```

If it is deployed to Microsoft Azure, `gunicorn --bind=0.0.0.0 --timeout 600 flask_app:app` must be added to `Startup Command` at `Configuration -> General settings` of the Web App.


## Remarks
Reference: https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-with-flask-and-sqlite

1. To run the application, type the followings in Terminal:
--------------------------------------------------------------
python flask_app.py
--------------------------------------------------------------
or
--------------------------------------------------------------
set FLASK_APP=flask_app
set FLASK_DEBUG=1
flask run
--------------------------------------------------------------
Debug mode will allow us to edit our files without constantly restarting the web server.

2a. For database using sqlite, install sqlite first.
Type the following code on schema.sql
--------------------------------------------------------------
DROP TABLE IF EXISTS table_posts;

CREATE TABLE table_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL
);
--------------------------------------------------------------

2b. To create databsae.db, type the following code on the terminal:
--------------------------------------------------------------
sqlite3 database.db < schema.sql
--------------------------------------------------------------

2c. Remark: To check data type of a table, the SQL command is:
--------------------------------------------------------------
PRAGMA table_info(your_table_name);
--------------------------------------------------------------

3. Display local time for timestamp and make use of Markdown for content text
--------------------------------------------------------------
@app.route('/')
def index():
    conn = db_conn()
    # to display the time stamp in local time --> datetime(your_column_name, 'localtime') as column_name
    notes = conn.execute("SELECT content, datetime(time_stamp, 'localtime') as time_stamp FROM table_posts ORDER BY time_stamp DESC").fetchall()
    conn.close()

    # transfer content to markdown format
    posts = []
    for note in notes:
        note = dict(note)
        note['content'] = markdown.markdown(note['content'])
        posts.append(note)
    # END transfer content to markdown format

    return render_template('index.html', posts=posts)
--------------------------------------------------------------

4. Prepare your flask app to be deployed
In git bash type the following. This creates a file called requirements.txt which contains all the dependencies for your project.
--------------------------------------------------------------
pip freeze > requirements.txt
--------------------------------------------------------------

