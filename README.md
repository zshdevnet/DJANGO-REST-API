# Photo Gallery Django Project

A Django web application that allows users to view photos in a gallery and like/dislike them. The project consists of two main apps: `photos` (API backend) and `gallery` (frontend interface).

## 🚀 Features

- **Photo Gallery**: Display uploaded photos with titles
- **Like/Dislike System**: Interactive voting system for photos
- **REST API**: Backend API for photo management
- **Image Upload**: Support for image file uploads
- **Admin Interface**: Django admin for managing photos

## 📋 Prerequisites

Before running this project, make sure you have:

- **Python 3.8+** installed on your system
- **pip** (Python package installer)
- Basic knowledge of Django framework

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd likeproject
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at:
- **Main Gallery**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Endpoints**: http://127.0.0.1:8000/api/

## 📁 Project Structure

```
likeproject/
├── likeproject/          # Main Django project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── photos/              # Photos app (API backend)
│   ├── models.py        # Photo model definition
│   ├── views.py         # API views
│   ├── urls.py          # API URL routing
│   └── serializers.py   # API serializers
├── gallery/             # Gallery app (frontend)
│   ├── views.py         # Gallery views
│   ├── urls.py          # Gallery URL routing
│   └── templates/       # HTML templates
├── media/               # Uploaded files storage
├── db.sqlite3          # SQLite database
├── requirements.txt    # Python dependencies
└── manage.py          # Django management script
```

## 📚 Dependencies & Libraries

### Core Dependencies

| Library | Version | Purpose | Import Usage |
|---------|---------|---------|--------------|
| **Django** | 5.2.4 | Main web framework | `from django.shortcuts import render` |
| **djangorestframework** | 3.16.0 | REST API framework | `from rest_framework import serializers` |
| **Pillow** | 11.3.0 | Image processing | `from PIL import Image` (used by Django ImageField) |
| **requests** | 2.31.0 | HTTP library for API calls | `import requests` |

### Development Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| **black** | 25.1.0 | Code formatter |
| **click** | 8.2.1 | Command line interface toolkit |
| **colorama** | 0.4.6 | Cross-platform colored terminal text |
| **mypy_extensions** | 1.1.0 | Type checking extensions |
| **packaging** | 25.0 | Core utilities for Python packages |
| **pathspec** | 0.12.1 | File path pattern matching |
| **platformdirs** | 4.3.8 | Platform-specific directory locations |

### Django Built-in Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| **asgiref** | 3.9.0 | ASGI utilities |
| **sqlparse** | 0.5.3 | SQL parsing |
| **tzdata** | 2025.2 | Timezone data |

## 🔧 Configuration

### Environment Variables
The project uses Django's default settings. For production, consider setting:

```python
# In settings.py
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
```

### Media Files
- **Upload Directory**: `media/photos/`
- **Media URL**: `/media/`
- **Supported Formats**: All image formats supported by Pillow

## 🎯 Usage

### Adding Photos
1. Access the admin interface at http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Navigate to "Photos" section
4. Click "Add Photo" and upload an image with a title

### Viewing Gallery
1. Visit http://127.0.0.1:8000/
2. Browse uploaded photos
3. Click "Like" or "Dislike" buttons to vote

### API Endpoints
- `GET /api/photos/` - List all photos
- `POST /api/photos/{id}/like/` - Like a photo
- `POST /api/photos/{id}/dislike/` - Dislike a photo

## 🐛 Troubleshooting

### Common Issues

1. **Import Error for requests**
   ```bash
   pip install requests==2.31.0
   ```

2. **Pillow Installation Issues (Windows)**
   ```bash
   pip install --upgrade pip
   pip install Pillow==11.3.0
   ```

3. **Database Migration Errors**
   ```bash
   python manage.py makemigrations --empty photos
   python manage.py migrate
   ```

4. **Media Files Not Loading**
   - Ensure `MEDIA_URL` and `MEDIA_ROOT` are properly configured
   - Check file permissions on the media directory

### Development Tips

- Use `python manage.py shell` for interactive Django shell
- Enable debug mode for detailed error messages
- Check Django logs in the console for debugging

## 🔒 Security Notes

- **Development Only**: This setup is for development purposes
- **Production**: Change `SECRET_KEY`, disable `DEBUG`, configure proper `ALLOWED_HOSTS`
- **File Uploads**: Implement proper file validation for production use

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review Django documentation
3. Create an issue in the repository

---

**Happy Coding! 🚀** 