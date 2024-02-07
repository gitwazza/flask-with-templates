# This Flask application builds on the flask example here:
# https://replit.com/@warrensutton/firstflask .
# This program separates out the HTML code and locates the HTML content in
# files within the "templates" folder. Doing so means that "render_template" needs
# to be imported from flask.
# In addition, the program uses Jinja as this allows values or data to be passed
# from this Python module, and be dynamically embedded in the various html pages.
# The program avoids the use of CSS and JavaScript.
# As per the example on replit, the web interface allows data to be entered and
# this can be passed to this program by use of a HTML form.
# Where data needs to be passed from the web interface to the Python module which
# is different from what a form will allow for then it may be necessary to utilise
# JavaScript, and this will be demonstrated in a further project.
#
# Created by Warren Sutton on 7 Feb 2024

from flask import Flask, request, render_template

app = Flask(__name__)

names = ['fred','bob','tom']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/book',methods=["POST","GET"])
def book():
  if request.method == 'POST':
    gname = request.form["name_input"]
    names.append(gname)
    return render_template("bookp.html", gname=gname)

  if request.method == 'GET':
    return render_template("bookg.html")

@app.route('/list')
def list():
  return render_template("list.html", name_list=names)

if __name__ == '__main__':
    app.run()
