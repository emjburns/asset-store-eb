from asset import *

class AssetStore :
    database = dict()

    def __str__ (self) :
        return str(self.database)

    def addAsset (self, asset):
        # Validate uniqueness
        if ( asset.assetName in self.database ) :
            return False
        self.database[asset.assetName] = asset
        return True

    def getAsset(self, assetName):
        if (assetName not in self.database):
            return None
        return self.database[assetName]

    def getAll(self):
        return self.database.values()
