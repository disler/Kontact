from flask import Flask, render_template, current_app, Response, request
from DBInterface import DBInterface
import json
import ast
from Validator import Validator
from WebUtil import WebUtil

app = Flask(__name__)

db = DBInterface()
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
    oRecord = db.GetByID("tblKontact", id)
    if(oRecord is None): oRecord = dict({})
    return WebUtil.AsJson(oRecord)

@app.route('/kontacts', methods=["POST"]) 
def Create():
    """
        Create a new kontact record
    """
    oKontact = WebUtil.ToJson(request.data)
    bValid = validator.Validate(oKontact)
    if bValid:
        db.Create("tblKontact", oKontact)
        return WebUtil.SuccessResponse()
    else:
        return WebUtil.FailureResponse()

@app.route("/kontacts/<int:id>", methods=["PUT"])
def Update(id):
    """
        Update a currently existing kontact record
    """
    oNewKontact = WebUtil.ToJson(request.data)
    oPreviousKontact = db.GetByID("tblKontact", id)
    print(oPreviousKontact)
    if(oPreviousKontact is not None):
        oMergedKontact = WebUtil.MergeDict(oPreviousKontact, oNewKontact)
        bValid = validator.Validate(oMergedKontact)
        print (bValid)
        if bValid:
            db.Update("tblKontact", id, oMergedKontact) 
            return WebUtil.SuccessResponse()
        else:
            return WebUtil.FailureResponse()
    else:
        return WebUtil.FailureResponse()

@app.route("/kontacts/<int:id>", methods=["DELETE"])
def Delete(id):
    """
        Delete a kontact based on it's id'
    """
    db.Delete("tblKontact", id)
    return WebUtil.SuccessResponse()



if __name__ == '__main__':
    app.run(debug=True)
