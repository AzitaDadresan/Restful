#!/usr/bin/python
import json
import pymongo
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson import json_util
import bottle
from bottle import route, run, request, abort

#Create Method
@route('/create', method='POST')
def create():
 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    ticker1=request.query.ticker
    date=request.query.date
    industry1=request.query.industry
    name2=request.query.company
    name3=request.query.comment
    
    result=collection.save({
        "Ticker" :ticker1,
        "Industry" : industry1,
        "Company" : name2.replace('%',''),
        "date" : date,
        "Comment" : name3.replace('%','')
        })
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
#Read Method
@route('/read', method='GET')
def read():
 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    name=request.query.business_name
    result=collection.find_one({"Ticker": name.replace('%','')})
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
  
#Update Method
@route('/update', method='GET')
def update():
 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    ticker2=request.query.tickerss
    condition1=request.query.condition
    result=collection.update({"Ticker" : ticker2},{"$set": {"Industry" : condition1.replace('%','')}}, upsert=True)
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
  
#Delete Method
@route('/delete', method='GET')
def delete():
 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    ticker3=request.query.tickers
    result=collection.delete_One({"Ticker": ticker3})
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
  
  
