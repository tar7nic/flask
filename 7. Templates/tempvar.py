from flask import Flask, render_template

app = Flask(__name__, template_folder="C://Users//Asus//OneDrive//Documents//VSC//output//.vscode//Flask//7. Templates")

@app.route('/')
def index():
    name = "Tarun"
    letters = list(name)
    pup_dict = {'pup_name':'Sammy'}
    return render_template('tempvar.html',name = name, letters = letters, pup_dict = pup_dict)

if __name__ == '__main__':
    app.run(debug = True) 
     