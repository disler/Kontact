from flask import Flask, render_template, current_app, Response, request
from server.DBInterface import DBInterface
from server.Validator import Validator
from server.WebUtil import WebUtil
import json
import ast

app = Flask(__name__)

#load database interface
db = DBInterface()

#load validator
validator = Validator.Kontact()

@app.route('/')
def Home(): 
    """
        Landing page for application
    """
    return current_app.send_static_file("index.html")

@app.route('/kontacts')
def Get():
    """
        Get the list of kontacts
    """
    return WebUtil.AsJson(db.Get("tblKontact"))

@app.route('/kontacts/<int:id>')
def GetByID(id):
    """
        Get single record by id
    """

    #get record by id from the kontact table
    oRecord = db.GetByID("tblKontact", id)

    #if the record returned is nothing return an empty object
    if(oRecord is None): 
        oRecord = dict({})

    return WebUtil.AsJson(oRecord)

@app.route('/kontacts', methods=["POST"]) 
def Create():
    """
        Create a new kontact record
    """

    #convert request data to json to be rendered as a python dict
    oKontact = WebUtil.ToObject(request.data)

    #if our processed data is a dict
    if type(oKontact) is dict:

        #validate to proper data structure
        bValid = validator.Validate(oKontact)

        #if valid kontact object is valid add to db
        if bValid:

            #create kontact obj
            db.Create("tblKontact", oKontact)

            #return success response
            return WebUtil.SuccessResponse()

        #kontact object is not valid return failure response
        else:
            return WebUtil.FailureResponse()

@app.route("/kontacts/<int:id>", methods=["PUT"])
def Update(id):
    """
        Update a currently existing kontact record
    """
    
    #Convert request to python structure
    oNewKontact = WebUtil.ToObject(request.data)
    
    #get current kontact we're going to update
    oPreviousKontact = db.GetByID("tblKontact", id)

    #if the kontact we're trying to update exists
    if(oPreviousKontact is not None):

        #combine the old kontact with the new - new having priority
        oMergedKontact = WebUtil.MergeDict(oPreviousKontact, oNewKontact)

        #validate the newly merged kontact object
        bValid = validator.Validate(oMergedKontact)
        
        #if the kontact object is valid
        if bValid:

            #update the kontact object
            db.Update("tblKontact", id, oMergedKontact)

            #return failure response
            return WebUtil.SuccessResponse()
        
        #kontact object is not valid
        else:

            #return failure response
            return WebUtil.FailureResponse()

    #the kontact we're trying to update does not exists return failure response
    else:
        return WebUtil.FailureResponse()

@app.route("/kontacts/<int:id>", methods=["DELETE"])
def Delete(id):
    """
        Delete a kontact based on it's id'
    """
    
    #get current kontact we're going to delete
    oPreviousKontact = db.GetByID("tblKontact", id)

    #if the kontact we're trying to delete exists
    if(oPreviousKontact is not None):

        #delete the kontact
        db.Delete("tblKontact", id)

        #return success response
        return WebUtil.SuccessResponse()

    #kontact does not exists return failure response
    else:
        return WebUtil.FailureResponse()


#launch flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
