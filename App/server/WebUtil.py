import json
from flask import Response
import ast
from random import randint


class WebUtil(object):
    """
        Provides web validation, response, generation, and conversion utility methods
    """
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
    def ToObject(sContent):
        """
            Safetly converts content from string to python literal structures ie string, number, tuple, list, dict, bool and none
        """
        return ast.literal_eval(sContent)

    @staticmethod
    def MergeDict(oBase, oOverwriter):
        """
            Merge two dictionaries with 'oOverwriter' overwriting the 'oBase' dictionary
        """
        #copy the object to be overwritten 
        oMerged = oBase.copy()

        #overwrite and add any fields to the 'oMerged' object from the 'oOverwrite' object
        oMerged.update(oOverwriter)

        return oMerged
    
    @staticmethod
    def GenerateNumber(iLength):
        """
            Generate a random number of length N
        """
        #lower bound of number length to create based of length
        iLowBound = 10 ** (iLength - 1)

        #upper bound of number length to create based on length
        iHighBound = (10 ** iLength) - 1

        #return random of lower and upper bound
        return randint(iLowBound, iHighBound)

