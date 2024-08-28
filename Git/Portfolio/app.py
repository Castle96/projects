from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {'title': 'Project 1', 'description': 'Description of project 1'},
        {'title': 'Project 2', 'description': 'Description of project 2'},
        {'title': 'Project 3', 'description': 'Description of project 3'}
    ]
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
