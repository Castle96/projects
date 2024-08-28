from flask import Flask, render_template

app = Flask(__name__)

#path to the home page of the project
@app.route('/')
def home():
  projects = [{'title': 'project1','description': 'Description of Project'},
   {'title': 'project2','description': 'Description of Project'},
   {'title': 'project3','description': 'Description of Project'}
  ]
  return render_template('index.html',projects=projects)

  @app.route('/about')
  def about():
    return render_template('about.html',title='About')


  @app.route('/contact')
  def contact():
    return render_template('contact.html',title='Contact')

  if __name__ == '__main__':
    app.run(debug=True)