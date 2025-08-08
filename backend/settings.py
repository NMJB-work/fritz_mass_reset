import os

API_TOKEN = os.environ.get('API_TOKEN', 'change_me_to_a_strong_token')
SELENIUM_URL = os.environ.get('SELENIUM_URL', 'http://localhost:4444/wd/hub')
USE_TLS = os.environ.get('USE_TLS', 'false').lower() in ('1', 'true', 'yes')
TLS_CERT = os.environ.get('TLS_CERT', '/app/certs/cert.pem')
TLS_KEY = os.environ.get('TLS_KEY', '/app/certs/key.pem')
DATA_DIR = os.environ.get('DATA_DIR', '/app/data')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

os.makedirs(DATA_DIR, exist_ok=True)
SELECTOR_PROFILES_FILE = os.path.join(DATA_DIR, 'selector_profiles.json')
