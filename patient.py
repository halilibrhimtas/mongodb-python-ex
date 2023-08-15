# Write to terminal "pip install pymongo pandas bson" for install mongodb 
#Import - pymongo and pandas
import pymongo
from bson.objectid import ObjectId;

#MongoDB Connection
client = pymongo.MongoClient("mongodb://mongodb_ip:27017/")

#Database connection
database = client["hospital"]

#Collection connection
patients = database["patients"]

#Task 1 - Post data to collection

patients.insert_many([
    {
        "first_name": "John",
        "last_name": "Smith",
        "age": 35,
        "medical_history": [
            {
                "disease": "Hypertension",
                "treatment": "Medication"
            },
            {
                "disease": "Diabetes",
                "treatment": "Diet and medication"
            }
        ]
    },
    {
        "first_name": "Emily",
        "last_name": "Johnson",
        "age": 28,
        "medical_history": [
            {
                "disease": "Asthma",
                "treatment": "Inhaled medications"
            },
            {
                "disease": "Migraine",
                "treatment": "Pain relief medication"
            }
        ]
    },
    {
        "first_name": "Michael",
        "last_name": "Davis",
        "age": 42,
        "medical_history": [
            {
                "disease": "Heart Disease",
                "treatment": "Surgery and medication"
            },
            {
                "disease": "High Cholesterol",
                "treatment": "Diet and medication"
            }
        ]
    }
]
)

# Task 2 - Update one patient data of name, age and medical history


#filter query
filter_query = {"_id": ObjectId("64da25f25667016e0b12b10b")}

#update query
update_query = {"$set" : {"first_name": "Sarah", "last_name": "Miller", "age": 30, "medical_history": [
            {
                "disease": "Allergies",
                "treatment": "Antihistamines"
            },
            {
                "disease": "Anxiety",
                "treatment": "Therapy and medication"
            }
        ]}}

patients.update_one(filter_query, update_query)


#Task 3 - Find all patients age > 30
  

data = patients.find({"age": {"$gt": 30}})
for a in data:
    print(a)
    


#Task 4 - Delete patients got a Migraine as a disease

query = {'medical_history.disease' : 'Migraine'}

patients.delete_many(query)
