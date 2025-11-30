import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.getcwd(), 'GestorDoTempo'))

try:
    from core.config import Config
    print("Config class imported successfully.")
    print(f"DEBUG: {Config.DEBUG}")
    print(f"DB_NAME: {Config.DB_NAME}")
    print(f"DB_USER: {Config.DB_USER}")
    # Don't print sensitive info like passwords in full, just check if it exists
    print(f"DB_PASSWORD set: {bool(Config.DB_PASSWORD)}")
except Exception as e:
    print(f"Error: {e}")
