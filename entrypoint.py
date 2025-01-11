import json  # Allows working with JSON data: encoding and decoding between Python dictionaries and JSON.
import redis as redis  # Imports the Redis Python client, enabling interaction with a Redis server.
from flask import Flask, request  # Imports Flask to create a web application and request to handle incoming web requests.
from loguru import logger  # Logging is used to record and store messages about the application's operation for troubleshooting and monitoring.


#Contants 
HISTORY_LEN =10
DATA_KEY= "engine_temperature"


#Creating Flask server and allow to interact with it using app variable
app= Flask( __name__) #Create instancer and __name__ is a special varaible that is used as starting point for flask to locate it resources


#Define an endpoint which accpets post requests and is reachable from /record endpoint

@app.route('/record',methods=['POST']) #Defines route Route that only respond to post requests for submiting data

def record_engine_temperature(): #function to handle the /record request 
    payload = request.get_json(force=True) #get json data from request
    logger.info(f"(*) Record Request --- {json.dumps(payload)} (*)") #log the raw request data

    engine_temperature= payload.get("engine_temperature") #extract the engine temp data
    logger.info(f"(*) engine temperature record is : {engine_temperature}") #log extracted temp

    #connect to Redis 
    database= redis.Redis(host="redis",port=6379,db=0,decode_responses=True)
    
    database.lpush(DATA_KEY,engine_temperature) #push new temp to redis list
    logger.info(f"stashed engine temperature in redis: {engine_temperature}") #log the action of storign

    #ensure only the latest 10 record are stored
    while database.llen(DATA_KEY) > HISTORY_LEN:
        database.rpop(DATA_KEY) #remove the oldest data
    engine_temperature_values= database.lrange(DATA_KEY,0,-1) #retrive all data from redis 
    logger.info(f"engine temperature list now contain these value {engine_temperature_values}")
    
    logger.info ("Record Record successful ")

    return {"success":True},200 #return a json payload and 200 status code to client 

@app.route('/collect',methods=['POST']) #similar to before but setsup collect route for post requests
def collect_engine_temperature():
    return{"success":True},200


