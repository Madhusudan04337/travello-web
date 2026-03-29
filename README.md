# 🌍 Travello - Premium Travel Agency Portal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white)

🚀 **Live Demo:** https://travello-web.onrender.com/

Travello is a full-stack travel booking application that allows users to explore destinations and manage travel offers. The system is built with Django and PostgreSQL, providing a scalable backend and a responsive user interface.

---

## ✨ KEY FEATURES

✅ **Secure Authentication** – User registration and login system with session management  
✅ **Contact Form** – Customer inquiry and message management system  
✅ **Cloudinary Media Storage** – Optimized cloud-based image hosting for destinations  
✅ **Admin Management** – Manage destinations, offers, and prices through Django Admin  
✅ **Responsive UI** – Mobile, tablet, and desktop compatibility  
✅ **Production Deployment** – Hosted on Render with PostgreSQL database  
✅ **Static File Management** – Efficient serving using WhiteNoise  

---

## 🛠 TECHNOLOGY STACK

| Category | Technology |
|----------|-----------|
| **Backend** | Django 4.2+ |
| **Database** | PostgreSQL |
| **Media Storage** | Cloudinary |
| **Hosting** | Render |
| **Static Files** | WhiteNoise |
| **Frontend** | HTML5, CSS3, JavaScript |

---

## 📂 PROJECT STRUCTURE

```
travello_web/
│
├── accounts/              # Authentication (login, register, logout)
├── contact/               # Contact form and message management
├── assets/                # Production static assets
├── media/                 # Uploaded media files
├── places/                # Destination logic and models
├── static/                # CSS / JS / images
├── templates/             # HTML templates
├── travello_web/          # Django settings and configuration
│   ├── settings.py        # Main settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
│
├── .env                   # Environment variables (not in git)
├── .gitignore             # Git ignore rules
├── db.sqlite3             # Local development database
├── manage.py              # Django management utility
├── Procfile               # Production start configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ LOCAL DEVELOPMENT SETUP

### 1. Clone Repository
```bash
git clone https://github.com/Madhusudan04337/travello-web.git
cd travello-web
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

**Activate Virtual Environment:**

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://user:password@localhost:5432/travello_db
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

**For Local Development (SQLite):**
```env
DEBUG=True
SECRET_KEY=your_secret_key_here
# Leave DATABASE_URL empty to use SQLite
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server
```bash
python manage.py runserver
```

**Visit:**  
🌐 Application: http://127.0.0.1:8000  
🔐 Admin Panel: http://127.0.0.1:8000/admin

---

## 🚀 DEPLOYMENT ON RENDER

### Step-by-Step Deployment Guide

#### 1. Push Project to GitHub
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

#### 2. Create PostgreSQL Database on Render
- Go to [Render Dashboard](https://dashboard.render.com/)
- Click **"New +"** → **"PostgreSQL"**
- Configure database and copy the **Internal Database URL**

#### 3. Create Web Service on Render
- Click **"New +"** → **"Web Service"**
- Connect your GitHub repository
- Configure the following:

**Build Settings:**
```bash
Build Command:
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Start Command:
gunicorn travello_web.wsgi:application
```

#### 4. Add Environment Variables

Navigate to **Environment** tab and add:

```
SECRET_KEY=your_production_secret_key
DEBUG=False
DATABASE_URL=your_render_postgres_internal_url
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
ALLOWED_HOSTS=travello-web.onrender.com
```

#### 5. Deploy
- Click **"Create Web Service"**
- Wait for build to complete
- Your app will be live at: `https://your-app-name.onrender.com`

---

## 📦 DEPENDENCIES

### Core Requirements
```txt
Django>=4.2
psycopg2-binary>=2.9
gunicorn>=21.2.0
whitenoise>=6.6.0
cloudinary>=1.36.0
python-decouple>=3.8
dj-database-url>=2.1.0
```

**Install all dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🗃️ DATABASE MODELS

### Places App
```python
class Destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.BooleanField(default=False)
```

### Accounts App
```python
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Additional custom fields
```

### Contact App
```python
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🔐 SECURITY FEATURES

✅ CSRF Protection enabled  
✅ Secure password hashing with Django's built-in system  
✅ Environment-based configuration using python-decouple  
✅ SQL injection protection via Django ORM  
✅ XSS protection through template auto-escaping  
✅ Production-ready security settings for Render deployment  

---

## 🎨 FRONTEND FEATURES

- **Responsive Design** – Mobile-first approach
- **Modern UI/UX** – Clean and intuitive interface
- **Dynamic Content** – AJAX-based interactions
- **Image Optimization** – Cloudinary CDN integration
- **Fast Loading** – WhiteNoise static file compression

---

## 🧪 TESTING

### Run Tests
```bash
python manage.py test
```

### Test Coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📊 ADMIN PANEL FEATURES

Access at: `/admin`

**Capabilities:**
- Manage destinations (add, edit, delete)
- View user registrations
- Review contact form submissions
- Monitor application statistics
- Manage media files via Cloudinary

---

## 🐛 TROUBLESHOOTING

### Common Issues

**Issue: Static files not loading in production**
```bash
python manage.py collectstatic --noinput
```

**Issue: Database connection error**
- Verify `DATABASE_URL` in environment variables
- Check PostgreSQL service status on Render

**Issue: Cloudinary images not displaying**
- Confirm `CLOUDINARY_CLOUD_NAME`, `API_KEY`, and `API_SECRET`
- Check Cloudinary dashboard for upload errors

**Issue: 500 Internal Server Error**
- Check Render logs: Dashboard → Your Service → Logs
- Verify all environment variables are set correctly

---

## 🔄 UPDATES & CHANGELOG

### Version 2.0 (Latest - March 2026)
✨ Added contact form with email notifications  
✨ Integrated Cloudinary for media management  
✨ Deployed to Render with PostgreSQL  
✨ Enhanced security with environment-based config  
✨ Improved responsive design for mobile devices  
✨ Added WhiteNoise for static file serving  

### Version 1.0
🚀 Initial release with basic features  
🚀 User authentication system  
🚀 Destination browsing functionality  

---

## 📝 LICENSE

This project is licensed under the MIT License.

---

## 🤝 CONTRIBUTING

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 CONTACT & SUPPORT

**Madhusudan S**  
💼 Full Stack Developer | Django Specialist | PostgreSQL Expert  

📧 Email: madhusudan04337@gmail.com  
🔗 GitHub: [@Madhusudan04337](https://github.com/Madhusudan04337)  
🌐 Portfolio: [Coming Soon]  

**For Issues:**  
Please open an issue on GitHub or contact via email.

---

## 🌟 ACKNOWLEDGMENTS

- Django Framework Team
- PostgreSQL Community
- Cloudinary Media Platform
- Render Hosting Service
- Open Source Contributors

---

## 📸 SCREENSHOTS

### 🏠 Homepage
![Homepage](./screenshots/homepage.png)

### 📞 Contact Page
![Contact](./screenshots/contact.png)

### 📝 Register Page
![Register](./screenshots/register.png)

### 🔐 Login Page
![Login](./screenshots/login.png)

### 📧 Forgot Password Email
![Email](./screenshots/email.png)

### ⚙️ Admin Panel (Backend)
![Admin](./screenshots/admin.png)

---

## 🚀 FUTURE ENHANCEMENTS

- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Booking management system
- [ ] Email confirmation for registrations
- [ ] Advanced search and filtering
- [ ] User profile dashboard
- [ ] Review and rating system
- [ ] Multi-language support
- [ ] Mobile app (React Native)
- [ ] AI-powered travel recommendations

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by **Madhusudan S**

© 2026 Travello Web. All Rights Reserved.

</div>