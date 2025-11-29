import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to manage environment variables and settings.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

    # Database Configuration
    DB_NAME = os.getenv('DB_NAME', 'gestordotempo_db')
    DB_USER = os.getenv('DB_USER', 'gestordotempo')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '!GestorDoTempo123!')
    DB_HOST = os.getenv('DB_HOST', 'integramaker.ifpb.edu.br')
    DB_PORT = os.getenv('DB_PORT', '8999')
