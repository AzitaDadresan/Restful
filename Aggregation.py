import json
import pymongo
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#Aggregate the matched sector and group it by Industry and result the total shares outstanding
#for each industry. 
def aggregation_document(document):
  try:
    sector=input("Enter Sector: ")
    query1 = {'$match':{"Sector":sector}}
    query2 = {'$group':{'_id':"$Industry",'all':{'$sum':"$Shares Outstanding"}}}
    query = [query1,query2]
    result=collection.aggregate(query)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    
print aggregation_document();

