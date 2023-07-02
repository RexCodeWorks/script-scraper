import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('./shotify-4245d-firebase-adminsdk-vvqvk-7eaea4556b.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()



data = {"content": "Hello World", "createdBy": "Rex", "fileName": "audio.wav"}

db.collection("transcripts").document().set(data)