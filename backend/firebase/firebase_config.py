import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate('path/to/your/credentials.json')
firebase_admin.initialize_app(cred)