# 🌍 Travello - Premium Travel Agency Portal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

> **🚀 Live Demo:** [https://travello-web-production.up.railway.app/](https://travello-web-production.up.railway.app/)

**Travello** is a high-performance, full-stack travel booking application designed to provide a seamless experience for travelers to discover and book their dream destinations. Built with robustness and scalability in mind using Django and PostgreSQL.

---

## ✨ Key Features

*   **🔐 Secure Authentication**: Robust user registration and login system with email validation.
*   **🖼️ Dynamic Media Engine**: Integrated **Cloudinary** for optimized, high-speed image delivery and storage.
*   **📂 Content Management**: Powerful admin interface for easy management of destinations, offers, and pricing.
*   **📱 Responsive Interface**: A fully responsive UI ensuring a flawless experience across mobile, tablet, and desktop devices.
*   **☁️ Production Ready**: Optimized for cloud deployment on **Railway** with PostgreSQL.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) | Core application framework |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white) | Primary production database |
| **Media** | ![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=flat-square&logo=cloudinary&logoColor=white) | Cloud-based image management |
| **Hosting** | ![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white) | Cloud deployment platform |
| **Static Files** | **WhiteNoise** | Efficient static file serving |

---

## 📂 Project Architecture

A professional, modular structure ensuring maintainability and scalability.

```
travello_web/
│
├── 🔐 accounts/          # Authentication logic (Login, Register, Logout)
├── 📦 assets/            # Production ready static assets (Collected)
├── 🖼️ media/             # User uploaded media content
├── 📍 places/            # Destination management & core logic
├── 🎨 static/            # Development static files (CSS, JS, Images)
├── 📑 templates/         # Jinja2 HTML Templates
├── ⚙️ travello_web/      # Project configuration & Settings
│
├── 📝 .env               # Environment configuration
├── 🐘 db.sqlite3         # Local development database
├── 🚀 manage.py          # Django CLI utility
├── 🐳 Procfile           # Production entry point
└── 📦 requirements.txt   # Project dependencies
```

> **Note**: The application uses **SQLite** for local development and switches to **PostgreSQL** automatically in production environments.

---

## ⚙️ Local Development Setup

Follow these steps to get a copy of the project up and running on your local machine.

### 1. Prerequisites
*   Python 3.8+
*   Git

### 2. Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Madhusudan04337/travello-web.git
    cd travello-web
    ```

2.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    DEBUG=True
    SECRET_KEY=your_secure_secret_key
    
    # Database (Optional for local, uses SQLite default)
    DATABASE_URL=postgres://user:pass@host:port/db_name

    # Cloudinary Config (Required for images)
    CLOUDINARY_CLOUD_NAME=your_cloud_name
    CLOUDINARY_API_KEY=your_api_key
    CLOUDINARY_API_SECRET=your_api_secret
    ```

5.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Run Development Server**
    ```bash
    python manage.py runserver
    ```
    Access the app at `http://127.0.0.1:8000`

---

## 🚀 Deployment

This project is configured for seamless deployment on **Railway**.

### Deployment Steps
1.  Push your code to GitHub.
2.  Connect your repository to **Railway**.
3.  Add the environment variables (from the `.env` section) in the Railway dashboard.
4.  Railway will automatically detect the `Procfile` and `requirements.txt` to build and serve the application.

---

## 👨‍💻 Author

**Madhusudan S**
*   🚀 Full Stack Developer
*   🐍 Django Specialist
*   🐘 PostgreSQL Expert

---

<p align="center">
  Made with ❤️ by Madhusudan S
</p>
