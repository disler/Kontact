class Validator(object):
    """
        Mock validation class wrapper
    """
    class Kontact(object):
        """
            Handles mock validation logic for 'kontacts'
        """
        def __init__(self):
            self.MAX_FIELD_LENGTH = 10
            self.REQUIRED_FIELDS = ["firstname", "lastname"]

        def Validate(self, oRecord):
            """
                Mock validation a kontact object for valid db writes
            """
            #length check
            if len(oRecord) > self.MAX_FIELD_LENGTH:
                return False
            
            #required fields
            lstHasRequiredFields = [sField in oRecord for sField in self.REQUIRED_FIELDS]
            if False in lstHasRequiredFields:
                return False

            return True