# this is used for creating the website's backend
# of site and creating static and dynamic pages.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")

@app.route('/contact')

def contact():
    return render_template("email.html")

if __name__ == "__main__":
    app.run(debug=True)
