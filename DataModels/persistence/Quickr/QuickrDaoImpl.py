from DataModels.persistence.DBConnector import Connector
from DataModels.webcrawler.quickr import QuickerCrawler, QuickrService
from DataModels.webcrawler.quickr import Parser
__author__ = 'shaleen'

class QuickrDaoImpl (Connector):

    con = Connector()

    def __init__(self):
        self.db = self.con.generateDBConnector('QUICKR')
        self.db.autocommit(True)

    def getCursor(self):
        return self.db.cursor()

    def getInsertQueryTemplateTest(self, dictObj):
        placeholders = ', '.join(['%s'] * len(dictObj))
        columns = ', '.join(dictObj.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('new_table', columns, placeholders)
        return sql

    def populateAndExecuteTest(self, obj):
        str = self.getInsertQueryTemplateTest(obj)
        print str
        cur = self.getCursor()
        cur.execute(str, obj.values())
        print cur.fetchall()

    def getInsertQueryTemplate(self, dictObj):
        placeholders = ', '.join(['%s'] * len(dictObj))
        columns = ', '.join(dictObj.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (self.con.QUICKRTABLE, columns, placeholders)
        return sql

    def populateAndExecute(self, obj):
        str = self.getInsertQueryTemplate(obj)
        print str
        cur = self.getCursor()
        cur.execute(str, obj.values())
        print cur.fetchall()

service = QuickrService.QuickrService()
list =  service.readEvalLoop()
print list

# list = {}
# list['id'] = 3
# list['test'] = 'wow'

print QuickrDaoImpl().populateAndExecute(list[0])