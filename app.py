from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/production')
def production():
    return render_template('production.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True) 
    app.run(debug=True)