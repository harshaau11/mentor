from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder = 'template', static_folder = 'static')
Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)

