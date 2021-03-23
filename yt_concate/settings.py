import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('api_key')

DOWNLOADS_DIR = 'downlades'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
