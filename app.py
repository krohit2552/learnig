from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def start():
    return "this is Home Page"

@app.route('/main')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)