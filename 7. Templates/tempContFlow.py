from flask import Flask, render_template

app = Flask(__name__, template_folder="C://Users//Asus//OneDrive//Documents//VSC//output//.vscode//Flask//7. Templates")

@app.route('/')
def index():
    # mylist = [1,2,3,4,5]
    # puppies = ['Fluffy', 'Rufus', 'Abby', 'Jenny', 'Max'] #'Snuffy' can changed
    user_login = True #Can put false
    return render_template('tempContFlow.html',user_login = user_login)

if __name__ == '__main__':
    app.run(debug = True)