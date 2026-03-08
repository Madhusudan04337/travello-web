# 🌍 Travello - Premium Travel Agency Portal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white)

🚀 **Live Demo:** https://travello-web.onrender.com/

Travello is a full-stack travel booking application that allows users to explore destinations and manage travel offers. 
The system is built with Django and PostgreSQL, providing a scalable backend and a responsive user interface.

------------------------------------------------------------

✨ KEY FEATURES

• Secure Authentication – User registration and login system.  
• Cloudinary Media Storage – Optimized cloud-based image hosting.  
• Admin Management – Manage destinations, offers, and prices.  
• Responsive UI – Mobile, tablet, and desktop compatibility.  
• Production Deployment – Hosted on Render with PostgreSQL.

------------------------------------------------------------

🛠 TECHNOLOGY STACK

Backend      : Django  
Database     : PostgreSQL  
Media        : Cloudinary  
Hosting      : Render  
Static Files : WhiteNoise  

------------------------------------------------------------

📂 PROJECT STRUCTURE

travello_web/
│
├── accounts/        Authentication (login, register, logout)
├── assets/          Production static assets
├── media/           Uploaded media
├── places/          Destination logic
├── static/          CSS / JS / images
├── templates/       HTML templates
├── travello_web/    Django settings and configuration
│
├── .env             Environment variables
├── db.sqlite3       Local development database
├── manage.py        Django management utility
├── Procfile         Production start configuration
└── requirements.txt Python dependencies

------------------------------------------------------------

⚙ LOCAL DEVELOPMENT SETUP

1. Clone Repository

git clone https://github.com/Madhusudan04337/travello-web.git
cd travello-web

2. Create Virtual Environment

python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment

Create a `.env` file in the project root:

DEBUG=True
SECRET_KEY=your_secret_key

DATABASE_URL=postgres://user:pass@host:port/db_name

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

5. Apply Database Migrations

python manage.py migrate

6. Run Development Server

python manage.py runserver

Visit:
http://127.0.0.1:8000

------------------------------------------------------------

🚀 DEPLOYMENT (RENDER)

1. Push project to GitHub.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Add environment variables in Render:

SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_render_postgres_url

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

5. Build Command

pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

6. Start Command

gunicorn travello_web.wsgi:application

After deployment, your app will be live on Render.

------------------------------------------------------------

👨‍💻 AUTHOR

Madhusudan S  
Full Stack Developer  
Django Developer  
PostgreSQL Enthusiast  

------------------------------------------------------------

Made with ❤️ by Madhusudan S
"""
