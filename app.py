from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('about.html')

@app.route('/ASL-Teacher')
def hello_world():
    return render_template('ASL_Teacher.html')

if __name__ == '__main__':
    app.run(debug=True, port=7000)