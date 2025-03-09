'''
This code prints all questions stored in the DB.
To ensure the connection with DB, run: mongosh "Your MongoDB URI"
'''
import json
from pymongo import MongoClient

# URI string
MONGO_URI = "Your MongoDB URI"
client = MongoClient(MONGO_URI)

# database and collection
db = client['medical_history_db']
coll = db['questions']

# fetch all questions
cursor = coll.find()

# iterate code
for doc in cursor:
    print(json.dumps(doc, indent=4, default=str))

# Close the connection to MongoDB
client.close()
