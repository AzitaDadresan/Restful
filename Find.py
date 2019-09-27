# -*- coding: utf-8 -*-
import json
import pymongo
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util
import os, sys

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#find document method to find gt than small value and less than large value
def find_document(document):
  try:
#Input data and find the count of the result agreed with the condition    
    small=input("What's your smallest Value? ")
    large=input("What's your largest Value? ")
    result=collection.find({"50-Day Simple Moving Average":{"$gt":small,"$lt":large}}).count()
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    
print find_document();

