from flask import Flask, render_template

app = Flask(__name__, template_folder="C://Users//Asus//OneDrive//Documents//VSC//output//.vscode//Flask//7. Templates")

@app.route('/')
def index():
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug = True) 