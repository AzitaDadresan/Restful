import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def read_document(document):
  try:
    result=collection.find_one(document)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    
import datetime


def main():
  myDocument = {"business_name" : "New ACME Explosives"}
  
  print read_document(myDocument)
main()
