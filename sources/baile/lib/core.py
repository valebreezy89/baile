from baile import utils
class Library:
    '''Main media collection storage
    Manages library items, infos, provides item data etc
    '''
    _dbMgrRegister = dict(sqlite="baile.lib.sqlitemgr.Mgr")

    def __init__(self, config):
        
        dbMgrName = config["db_mgr"];
        if (self._dbMgrRegister.has_key(dbMgrName) == False):
            raise LibException("Unknown db_mgr name")
        mgrClass = self._dbMgrRegister[dbMgrName];
        self._dbMgr = utils.create_instance(mgrClass)
    
class DbMgr:
    '''Interface for any Data Base managers in the system'''
    def get_item_info(self, itemId):
        '''Returns info dict for given item, None if no such item was found'''
        pass
    def get_item_info_fields(self, itemId, fields):
        '''Returns particular info fields for given item, None if no such item was found'''
        pass
    def set_item_info(self, itemId, info):
        '''Set full info for given item'''
        pass
    def set_item_info_fields(self, itemId, fields):
        '''Set particular fields of item info'''
        pass
    
class LibException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

if (__name__ == "__main__"):
    l = Library(dict(db_mgr="sqlite"))