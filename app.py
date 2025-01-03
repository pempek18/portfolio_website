from flask import Flask, render_template, make_response
import python_pdfkit as pdfkit

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

@app.route('/generate_cv')
def generate_cv():
    # Render the template to HTML
    html = render_template('experience.html')
    
    # Configure PDF options if needed
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    }
    
    # Generate PDF from HTML
    pdf = pdfkit.from_string(html, False, options=options)
    
    # Create the response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cv.pdf'
    
    return response

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True) 
    app.run(debug=True)