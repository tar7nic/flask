from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1> Hello Puppy! <h1>"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h2> Puppies are cute! <h2>"

@app.route('/puppy/<name>')
def puppy(name):
    return f"100th letter: {name[100]}"

if __name__ == '__main__':
    app.run(debug=True)
    
'''debug=True use this only for your personal help, always 
set debug = False when for ready for production as it will 
show the debug page instead of server error to the users.'''
