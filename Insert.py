import json
import pymongo
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util


connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#update the document by inserting the information in myDocument in the document
#and save it.
def insert_document(document):
  try:
    result=collection.save(document)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    


def main():
  myDocument = {
        "Ticker" : "WBD",
        "Industry" : "Web Developers",
        "Company" : "Ryan Developers",
        "Comment" : "Newly Added Comment"
}
  print insert_document(myDocument)
main()
