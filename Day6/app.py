from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/portfolio')
def index():
    return render_template('index.html')

@app.route('/home')
def home_redirect():
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # Correct projects data from resume
    projects = [
        {
            'title': 'AI Powered Resume Analyzer Web App',
            'description': 'A comprehensive web application for resume analysis and career guidance.',
            'features': [
                'Independently built and launched application with complete system architecture responsibility',
                'Built scalable full-stack application using Django, deployed on Google Cloud Run (60+ users)',
                'Integrated Google Gemini API for dynamic skill recommendations and interview questions (20% improvement)',
                'Implemented OCR and NLP pipelines for resume parsing from multiple formats (90% accuracy)'
            ],
            'tech_stack': ['Python', 'Django', 'MySQL', 'HTML/CSS', 'Bootstrap', 'Google Cloud Run', 'Google Gemini API', 'OCR', 'NLP'],
            'github_link': 'https://github.com/ShaikSameerAhamad/SmartScreen-AI.git',
            'live_link': 'https://resume-analyzer-300042385047.us-central1.run.app/',
            'has_demo': True
        },
        {
            'title': 'Restaurant Management System',
            'description': 'A comprehensive restaurant management solution with real-time capabilities.',
            'features': [
                'Led development and coordination of 5-member team with successful timely delivery',
                'Designed JavaFX-based system using MVC architecture (60% improvement in UI responsiveness)',
                'Built real-time table and order modules (40% reduction in processing time)',
                'Integrated secure login, reservation, and menu systems with JavaFX bindings'
            ],
            'tech_stack': ['Java', 'JavaFX', 'PostgreSQL', 'MVC Architecture'],
            'github_link': 'https://github.com/ShaikSameerAhamad/RestaurantManagementSystem.git',
            'live_link': '#',
            'has_demo': False
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return render_template('contact.html')
        
        # Here you would typically send an email or save to database
        # For demo purposes, we'll just show a success message
        flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)