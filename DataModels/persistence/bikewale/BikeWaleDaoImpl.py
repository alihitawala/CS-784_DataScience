from DataModels.persistence.DBConnector import Connector
from DataModels.persistence.bikewale.DaoHelper import DaoHeper
__author__ = 'aliHitawala'
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Dao (Connector):

    con = Connector()

    def __init__(self):
        self.db = self.con.generateDBConnector('BIKEWALE')
        self.db.autocommit(True)
        self._helper = DaoHeper()

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
        columnNameList = self._helper.getKeyToColumnName(dictObj)
        placeholders = ', '.join(['%s'] * len(columnNameList))
        columns = ', '.join(columnNameList)
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (self.con.BIKEWALETABLE, columns, placeholders)
        return sql

    def populateAndExecute(self, dictObj):
        try:
            values = dictObj.values()
            str = self.getInsertQueryTemplate(dictObj)
            cur = self.getCursor()
            cur.execute(str, values)
        except:
            logger.error("DB query execution failed for an obj : " + dictObj)