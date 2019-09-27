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



def update_document():
  try:
    result=collection.update({"Ticker" : "A"},{"$set": {"Volume" : "534"}}, upsert=True)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    

print update_document();



def delete_document(document):
  try:
    result=collection.delete_One(document)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    


def main():
  myDocument = {"Ticker" : "BRLI"}
  
  print delete_document(myDocument)
main()


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


#find document method to find the exact industry and return the Tickers 
def find_ticker(document):
  try:
    industry=input("Industry:")
    result=collection.find({"Industry":industry},{"Ticker"}:1)
    return True;
  except ValidationError as ve:
    abort(400, str(ve))
    return result
    
print find_ticker();

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



#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort

#returns the stock of documents all as a summary.
@route('/stocks', method='POST')
def stocks(): 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    #query1 for sorting
    query1 = { '$project': { 'Ticker':1,'Performance (Quarter)':1,'Institutional Ownership':1,'Shares Outstanding':1,'Volume':1 } }
    #matches with the ticker
    query2 = { '$match': { "Ticker": ticker } }
    #query3 uses group to group and find sum, avg and other operations
    query3 = { '$group': { 'Ticker': "$Ticker", 'Total Shares Outstanding': {'$sum': "$Shares Outstanding" },
                           'Average Performance (Quarter)':{'$avg':"$Performance (Quarter)"},
                           'Institutional Ownership':{'$avg':'$Institutional Ownership'},
                           'Max Shares Outstanding':{'$max':'$Shares Outstanding'},
                           'Total Volume':{'$sum':'$Volume'} } }
    query = [query1,query2,query3] #formlates query
    result=collection.aggregate(query) 
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
  
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
  
  


  
  
#returns the summary of documents matching the ticker requested.
@route('/summary', method='GET')
def summary(): 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
    list1 = request.json.get('list') #retrieves the value of the list key 
    list1 = list1.replace("[","") #removes [
    list1 = list1.replace("]","") #removes ]
    list1 = list1(list1.split(",")) #create a list from the remaining list
    items = list1()
    #This for loop uses each ticker in the list
    for name in list1:
      print(name)
      item = getReport(name)
      print(item)
      items.append("Report For Ticker "+name+" \n"+item+"\n\n")
    return items #return a list of items
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
  
  
#returns the summary of documents matching the ticker requested.
@route('/top', method='GET')
def top(): 
  try:
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    
        #query1 for sorting
    query1 = { '$project': { 'Ticker':1,'Performance (Quarter)':1,'Institutional Ownership':1,'Shares Outstanding':1,'Volume':1 } }
    #matches with the ticker
    query2 = { '$match': { "Ticker": ticker } }
    #query3 uses group to group and find sum, avg and other operations
    query3 = { '$group': { 'Ticker': "$Ticker", 'Total Shares Outstanding': {'$sum': "$Shares Outstanding" },
                           'Average Performance (Quarter)':{'$avg':"$Performance (Quarter)"},
                           'Institutional Ownership':{'$avg':'$Institutional Ownership'},
                           'Max Shares Outstanding':{'$max':'$Shares Outstanding'},
                           'Total Volume':{'$sum':'$Volume'} } }
    
    #query4 detrmines number of items to deal with
    query4 = { '$limit' : 5 }
    query = [query1,query2,query3,query4]
    result=collection.aggregate(query)
    
  except NameError:
    abort(404, 'No parameter')
  
  if not string:
    abort(404, 'Not Found')
  return json.loads(json.dumps(string, indent=4, default=json_util.default))

if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  

  


