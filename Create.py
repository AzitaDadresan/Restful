import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def insert_document(document):
  try:
    result=collection.save(document)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    
import datetime

def main():
  myDocument = {
        "business_name" : "New ACME Explosives",
        "date" : "Jul 27 2019",
        "result" : "Business Re-opened",
        "Comments" : "Under new management"
}
  print insert_document(myDocument)
main()
