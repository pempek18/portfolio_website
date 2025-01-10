from flask import Flask, render_template, make_response
import pdfkit
import os

app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/experience')
def experience():
    return render_template('experience.html', active_page='experience')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html', active_page='technologies')

@app.route('/services')
def services():
    return render_template('services.html', active_page='services')

@app.route('/production')
def production():
    return render_template('production.html', active_page='production')

@app.route('/generate_cv')
def generate_cv():
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    
    # Add PDF-specific styles to hide buttons
    pdf_specific_styles = """
    <style>
        .menu a {
            display: none !important;
        }
        .cv-download {
            display: none !important;
        }
        .header-nav::before {
            font-family: 'Cascadia Code', monospace !important;
            color: var(--cv-grey) !important;
            content: "Patryk Zadroga Automation Engineer" !important;
            font-size: 3rem !important;
            font-weight: bold !important;
            text-align: center !important;
        }
    </style>
    """
    
    # Add the PDF styles to the HTML
    html = pdf_specific_styles + render_template('experience.html')
    
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'enable-local-file-access': True,
        'user-style-sheet': os.path.join(static_dir, 'styles.css'),
        'no-stop-slow-scripts': True,
        'javascript-delay': 1000,
        'load-error-handling': 'ignore',
        'load-media-error-handling': 'ignore'
    }
    
    # Update image path replacement to handle all images
    # Replace all static file URLs with absolute file paths
    for image in ['email.png', 'phone.png', 'github.png', 'location.png', 'profile.jpg']:
        html = html.replace(
            f'/static/img/{image}',
            'file:///' + os.path.join(static_dir, 'img', image).replace(os.sep, '/')
        )    
    # For debugging: you can uncomment this to see the processed HTML
    # with open('debug.html', 'w', encoding='utf-8') as f:
    #     f.write(html)
    
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cv.pdf'
    
    return response

if __name__ == '__main__':
    if os.path.basename(os.path.dirname(os.path.abspath(__file__))) == 'app':
        # For production in Docker container
        app.run(host='0.0.0.0', debug=False, port=8080)
    else:
        # For local development on Windows
        app.run(debug=True, port=8080)