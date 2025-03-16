Personal Website - Django
Overview
This Django-based personal website allows professionals to showcase their resume, educational background, work experience, blog posts, portfolio, and contact details. The website serves as a digital CV and personal brand hub.
Features
Resume Upload: Users can upload and display their resume in PDF format.
Education & Work Experience: Add and manage academic and professional background.
Portfolio Showcase: Display past projects with descriptions and images.
Blog System: Create and publish blog posts.
Contact Page: Visitors can reach out via a contact form.
Admin Dashboard: Manage content easily.
Technologies Used
Backend: Django, Django REST Framework
Database: PostgreSQL / SQLite
Frontend: HTML, CSS, Bootstrap
Authentication: Django’s built-in authentication system
Version Control: Git & GitHub
Installation & Setup  
1. Clone the repository:  
   `bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
.2 Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
.3 Install dependencies:
pip install -r requirements.txt
.4 Run migrations and start the server:
python manage.py migrate
python manage.py runserver
Future Improvements
Dark Mode UI: User preference for light/dark themes
SEO Optimization: Improve search engine visibility
Multilingual Support: Make the website accessible to a wider audience
