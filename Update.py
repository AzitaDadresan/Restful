import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def update_document():
  try:
    result=collection.update({"business_name" : "New ACME Explosives"},{"$set": {"Condition" : "Good"}}, upsert=True)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    

print update_document();
    
