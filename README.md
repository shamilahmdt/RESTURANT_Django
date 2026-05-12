# 🍽️ RESTURANT - Modern Restaurant Showcase

A premium, responsive restaurant web application built with **Django** and **Tailwind CSS**. This platform allows restaurant owners to showcase their culinary delights, categorize menus, and engage customers with a stunning, high-performance UI.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## ✨ Features

- **Dynamic Hero Section:** Engaging call-to-action for order placements.
- **Category Management:** Showcase food categories with dish counts and custom imagery.
- **Special Dishes Gallery:** Highlights top-rated menu items directly from the database.
- **Testimonials Section:** Build trust with customer feedback displays.
- **Admin Dashboard:** Effortless management of categories and menu items.
- **Responsive Design:** Fully optimized for mobile, tablet, and desktop views using Tailwind CSS.

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/shamilahmdt/RESTURANT_Django.git
cd RESTURANT_Django
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
The project uses **PostgreSQL**. Ensure you have a database named `djpt3` and update the credentials in `rest/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djpt3',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```

## 📂 Project Structure
- `rest/`: Project configuration and settings.
- `resturant/`: Main application logic (Models, Views, URLs).
- `templates/`: HTML templates featuring Tailwind CSS integration.
- `static/`: CSS, Images, and Javascript assets.
- `media/`: User-uploaded content (Food and Category images).

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---
Developed with ❤️ by [Shamil](https://github.com/shamilahmdt)
