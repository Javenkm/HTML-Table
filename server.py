from flask import Flask, render_template
app = Flask(__name__)

@app.route('/list')

def list():

    users = [
        {'first_name' : 'Javen', 'last_name' : 'Manning'},
        {'first_name' : 'Israel', 'last_name' : 'Vallejo'},
        {'first_name' : 'John', 'last_name' : 'Manning'},
        {'first_name' : 'Rhonda', 'last_name' : 'Manning'}
    ]
    return render_template("index.html", users = users)

if __name__=="__main__":
    app.run(debug=True)