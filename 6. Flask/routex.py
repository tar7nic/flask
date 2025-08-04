from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Puppies are cute"

@app.route('/<name>')
def name(name):
    return f"Puppy's name is {name}"

@app.route('/Latin/<name>')
def puppy_latin(name):
    if name[-1] != 'y':
        return f"Name in Puppy Latin is {name+'y'}"
    else:
        return f"Name in Puppy Latin is {name.replace(name[-1],'iful')}"
    
if __name__ == '__main__':
    app.run(debug=True)