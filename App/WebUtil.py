import json
from flask import Response
import ast
from random import randint


class WebUtil(object):
    @staticmethod
    def SuccessResponse():
        """
            Generic 200 code success response
        """
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
    @staticmethod
    def FailureResponse():
        """
            Generic 400 code 'bad data' response 
        """
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'} 

    @staticmethod
    def AsJson(sContent):
        """
            returns content to the view in json
        """
        return Response(json.dumps(sContent), mimetype='application/json')
    
    @staticmethod
    def ToJson(sContent):
        """
            Unsafely converts content from string to json content
        """
        return ast.literal_eval(sContent)

    @staticmethod
    def MergeDict(oBase, oOverwriter):
        """
            Merge two dictionaries with 'oOverwriter' overwriting the 'oBase' dictionary
        """
        oMerged = oBase.copy()
        oMerged.update(oOverwriter)
        return oMerged
    
    @staticmethod
    def GenerateNumber(iLength):
        """
            Generate a random number of length N
        """
        iLowBound = 10 ** (iLength - 1)
        iHighBound = (10 ** iLength) - 1
        return randint(iLowBound, iHighBound)

