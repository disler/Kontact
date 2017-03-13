import datetime
from server.WebUtil import WebUtil

class DBInterface(object):
    """
        Interface between external api layers and database
        NOTE: CURRENTLY IN MEMORY MOCK DATABASE
    """
    def __init__(self):
        self.GenerateMockKontacts()

    def GenerateMockKontacts(self):
        """
            Generate in memory kontacts
        """
        self.oTables = dict({"tblKontact" : self.GetKontactTable()})

    #GENERIC DATABASE ACCESS METHODS

    def Get(self, sTableName):
        """
            Retrieves all rows from a table
        """
        return self.oTables[sTableName]

    def GetByID(self, sTableName, id):
        """
            Get a record from a table based on it's id
        """

        #filter IN all records from table 'sTableName' that match the id 'id'
        lstRecord = list(filter(lambda _record: _record["id"] == id, self.oTables[sTableName]))

        #if we found a single record return it
        if len(lstRecord) == 1:
            return lstRecord[0]
        #if we found many or no records return none
        else:
            return None

    def Create(self, sTableName, oRecord):
        """
            Create a new record
        """

        #generate a random id and append it to the record
        oRecord["id"] = WebUtil.GenerateNumber(10)

        #append the record 'oRecord' into the table 'sTableName'
        self.oTables[sTableName].append(oRecord)

        return True

    def Update(self, sTableName, id, oRecord):
        """
            Update an element by replace it at it's index
        """

        #get the index of the record 'oRecord' in the table 'sTableName' that matches the id 'id'
        lstIndexOfRecordInDB = [iIndex for iIndex, _record in enumerate(self.oTables[sTableName]) if _record["id"] == id] 

        #if we found the record index, store it into 'iIndexOfRecord'
        if len(lstIndexOfRecordInDB) == 1:

            #record the index
            iIndexOfRecord = lstIndexOfRecordInDB[0]

            #overwrite the previous record with the record 'oRecord' in the table 'sTableName' in the index 'iIndexOfRecord'
            self.oTables[sTableName][iIndexOfRecord] = oRecord

        #we found more than one or no record with the matching id
        else:
            return False

        return True

    def Delete(self, sTableName, id):
        """
            Delete a record by filtering it out on it's id
        """

        #reset the table 'sTableName' to contain all records not including the one that matches the id of 'id'
        self.oTables[sTableName] = list(filter(lambda _record: _record["id"] != id, self.oTables[sTableName]))
        
        return True

    def GetKontactTable(self):
        """
            Separation method to fetch in memory mock elements
        """
        dtToday = datetime.date.today().strftime("%m/%d/%Y")
        return list([
                dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head1.jpg",
                    "color" : "#a3bcf7",
                    "firstname": "Dave",
                    "lastname": "Hanson",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "facebook" : dict({
                            "name" : "facebook",
                            "icon" : "/static/img/facebook.png",
                            "link" : "http://facebook.com"
                        }),
                        "twitter" : dict({
                            "name" : "twitter",
                            "icon" : "/static/img/twitter.png",
                            "link" : "http://twitter.com"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head4.jpg",
                    "color" : "#f9ec70",
                    "firstname": "Shelby",
                    "lastname": "Colden",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "youtube" : dict({
                            "name" : "youtube",
                            "icon" : "/static/img/youtube.png",
                            "link" : "http://youtube.com"
                        }),
                        "twitter" : dict({
                            "name" : "twitter",
                            "icon" : "/static/img/twitter.png",
                            "link" : "http://twitter.com"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head7.jpg",
                    "color" : "#7c2182",
                    "firstname": "Letuc",
                    "lastname": "WalBock",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "facebook" : dict({
                            "name" : "facebook",
                            "icon" : "/static/img/facebook.png",
                            "link" : "http://facebook.com"
                        }),
                        "twitter" : dict({
                            "name" : "twitter",
                            "icon" : "/static/img/twitter.png",
                            "link" : "http://twitter.com"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head8.jpg",
                    "color" : "#4c0182",
                    "firstname": "John",
                    "lastname": "Haller",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "youtube" : dict({
                            "name" : "youtube",
                            "icon" : "/static/img/youtube.png",
                            "link" : "http://youtube.com"
                        }),
                        "twitter" : dict({
                            "name" : "twitter",
                            "icon" : "/static/img/twitter.png",
                            "link" : "http://twitter.com"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head5.jpg",
                    "color" : "#22aa22",
                    "firstname": "Allen",
                    "lastname": "Sharp",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "linkedin" : dict({
                            "name" : "linkedin",
                            "icon" : "/static/img/linkedin.png",
                            "link" : "http://linkedin.com"
                        }),
                        "whatsapp" : dict({
                            "name" : "whatsapp",
                            "icon" : "/static/img/whatsapp.png",
                            "link" : "http://whatsapp.com"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head10.jpg",
                    "color" : "#83ddff",
                    "firstname": "Daniel",
                    "lastname": "Isler",
                    "date of birth" : datetime.datetime(1992, 12, 3).strftime("%d/%m/%Y"),
                    "zip-code" : 55427,
                    "media" : dict({
                        "youtube" : dict({
                            "name" : "youtube",
                            "icon" : "/static/img/youtube.png",
                            "link" : "https://www.youtube.com/user/daanIsl"
                        })
                    })
                }), dict({
                    "id" : WebUtil.GenerateNumber(10),
                    "face" : "/static/img/heads/head2.jpg",
                    "color" : "#aa2222",
                    "firstname": "Steve",
                    "lastname": "Willheart",
                    "date of birth" : dtToday,
                    "zip-code" : WebUtil.GenerateNumber(5),
                    "media" : dict({
                        "linkedin" : dict({
                            "name" : "linkedin",
                            "icon" : "/static/img/linkedin.png",
                            "link" : "http://linkedin.com"
                        }),
                        "whatsapp" : dict({
                            "name" : "whatsapp",
                            "icon" : "/static/img/whatsapp.png",
                            "link" : "http://whatsapp.com"
                        })
                    })
                })
            ])
