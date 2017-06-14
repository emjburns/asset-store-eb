import re
import structlog

logger = structlog.get_logger(__name__)

class Asset :
    def __init__(self, assetName = "", assetType = "", assetClass = ""):
        self.assetName = assetName
        self.assetType = assetType
        self.assetClass = assetClass

    def __str__(self):
        return "(name: " + str( self.assetName ) + ", " + \
                   "type: " + str( self.assetType ) + "," + \
                   "class: " + str(self.assetClass) + ")"

    def serialize(self):
        return {
            'assetName': self.assetName,
            'assetType': self.assetType,
            'assetClass': self.assetClass,
        }

    def validateAsset(self):
        # returns true/false and validation message
       message = ""
       if (len(self.assetName) < 4 or len(self.assetName) > 64 ):
           message += "Name needs to be 4-64 characters. "
           return (False, message)
       validName = False
       if (re.match("^[^_-][A-Za-z0-9_-]+$", self.assetName) != None):
           validName = True
       else:
           message += "Name must only contain alphanumeric ascii characters, underscores, and dashes. Also, name cannot start with an underscore or dash. "

       validType = (self.assetType == "satellite") or (self.assetType == "antenna")
       if (not validType):
           message += "Type must be either 'satellite' or 'antenna'. "

       validClass = False
       if (self.assetType == "satellite") :
           validClass = (self.assetClass == "dove") or (self.assetClass == "rapideye")
           if (not validClass):
               message+= "Class must be either 'dove' or 'rapideye'. "
       elif (self.assetType == "antenna") :
           validClass = (self.assetClass == "dish") or (self.assetClass == "yagi")
           if (not validClass):
               message+= "Class must be either 'dish' or 'yagi'. "
       return (validName and validType and validClass, message)
