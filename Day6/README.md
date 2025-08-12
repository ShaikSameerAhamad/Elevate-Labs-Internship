# Portfolio Website - Day 6

A personal portfolio website built with Flask, HTML, CSS, and Bootstrap.

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Multiple Pages**: Home, About, Projects, and Contact pages
- **Contact Form**: Functional contact form with validation
- **Modern UI**: Clean, professional design with animations
- **Project Showcase**: Display your projects with descriptions and tech stacks
- **Social Links**: Connect to your GitHub, LinkedIn, and other profiles

## Project Structure

```
Day6/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── projects.html     # Projects showcase
│   └── contact.html      # Contact form
├── static/               # Static files
│   └── css/
│       └── style.css     # Custom CSS styles
└── README.md            # This file
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Open in Browser**:
   Navigate to `http://127.0.0.1:5000`

## Customization

### Personal Information
Update the following placeholders in the templates:
- `[Your Name]` - Replace with your actual name
- `[Your City, Country]` - Your location
- `[Your Education]` - Your educational background
- `[your-email@example.com]` - Your email address

### Projects
Edit the `projects` list in `app.py` to showcase your actual projects:
```python
projects = [
    {
        'title': 'Your Project Name',
        'description': 'Project description',
        'tech_stack': ['Python', 'Flask', 'etc'],
        'github_link': 'https://github.com/yourusername/project'
    }
]
```

### Styling
- Modify `static/css/style.css` to change colors, fonts, and layout
- Update the color scheme by changing CSS variables in `:root`
- Add your own images by replacing placeholder content

### Contact Form
The contact form currently shows success messages. To make it functional:
1. Set up email configuration in `app.py`
2. Add SMTP settings for sending emails
3. Or integrate with a service like Formspree or Netlify Forms

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Styling**: Custom CSS with animations

## Next Steps

1. Add your personal information and projects
2. Upload your profile photos
3. Set up email functionality for the contact form
4. Deploy to a hosting service (Heroku, PythonAnywhere, etc.)
5. Add more sections like blog, testimonials, or resume download

## Deployment

To deploy this application:
1. Choose a hosting platform (Heroku, PythonAnywhere, DigitalOcean)
2. Set up environment variables for production
3. Configure a production WSGI server like Gunicorn
4. Set up a custom domain if desired

Enjoy building your portfolio website! 🚀