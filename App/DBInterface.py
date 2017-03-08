from time import time
from WebUtil import WebUtil

class DBInterface(object):
    """
        Handles direct data base operations
    """
    def __init__(self):
        self.oTables = {
            "tblKontact" : [
                dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "firstname": "Dave",
                    "lastname": "Hanson",
                    "date of birth" : time(),
                    "zip-code" : WebUtil.GenerateNumber(5)
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "firstname": "Shelby",
                    "lastname": "Colden",
                    "date of birth" : time(),
                    "zip-code" : WebUtil.GenerateNumber(5)
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "firstname": "Letuc",
                    "lastname": "WalBock",
                    "date of birth" : time(),
                    "zip-code" : WebUtil.GenerateNumber(5)
                })
            ]
        }

    #DATABASE ACCESS METHODS

    def Get(self, sTableName):
        """
            Retrieves all rows from a table
        """
        return self.oTables[sTableName]
    
    def GetPaginate(self, sTableName, iPage, iPageSize):
        """
            Retrieves a certain page of record 'sTableName' in specific amounts 'iPageSize'
        """
        pass

    def GetByID(self, sTableName, id):
        """
            Get a record from a table based on it's id
        """
        lstRecord = list(filter(lambda _record: _record["id"] == id, self.oTables[sTableName]))
        if len(lstRecord) == 1:
            return lstRecord[0]
        else:
            return None

    def Create(self, sTableName, oRecord):
        """
            Create a new record
        """
        oRecord["id"] = WebUtil.GenerateNumber(10)
        self.oTables[sTableName].append(oRecord)
        return True

    def Update(self, sTableName, id, oRecord):
        """
            Update an element by replace it at it's index
        """
        lstIndexOfRecordInDB = [iIndex for iIndex, _record in enumerate(self.oTables[sTableName]) if _record["id"] == id] 
        if len(lstIndexOfRecordInDB) == 1:
            iIndexOfRecord = lstIndexOfRecordInDB[0]
        self.oTables[sTableName][iIndexOfRecord] = oRecord
        return True

    def Delete(self, sTableName, id):
        """
            Delete a record by filtering it out on it's id
        """
        self.oTables[sTableName] = list(filter(lambda _record: _record["id"] != id, self.oTables[sTableName]))
        return True
