from flask import Flask # Import flask web framework

#Creating Flask server and allow to interact with it ussing app variable
app= Flask(__name__) #Create instancer and __name__ is a special varaible that is used as starting point for flask to locate it resources

#Define an endpoint which accpets post requests and is reachable from /record endpoint
@app.route('/record',methods=['POST']) #Defines route Route that only respond to post requests for submiting data

def record_engine_temperature(): #function to handle the /record request 
    pass

    #return a json payload and 200 status code to client 
    return {"success":True},200

@app.route('/collect',methods=['POST']) #similar to before but setsup collect route for post requests
def collect_engine_temperature():
    return{"success":True},200


