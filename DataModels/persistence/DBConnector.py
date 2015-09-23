__author__ = 'shaleen'

import MySQLdb
import abc

class Connector:

    QUICKRDB = 'test'
    QUICKRROOT = 'root'
    QUICKRPASS = 'help2012'
    QUICKRLOCAL = 'localhost'
    QUICKRTABLE = 'Quickr'


    def generateDBConnector(self, root):
        if root == 'QUICKR':
            return MySQLdb.connect(self.QUICKRLOCAL, self.QUICKRROOT, self.QUICKRPASS, self.QUICKRDB)

    @abc.abstractmethod
    def getCursor(self):
        return

    @abc.abstractmethod
    def getInsertQueryTemplate(self):
        return

    @abc.abstractmethod
    def populateAndExecute(self):
        return

# db = Connector().generateDBConnector('QUICKR')
#
# # prepare a cursor object using cursor() method
# cursor =  db.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("""INSERT INTO `test`.`new_table` (`id`, `test`) VALUES (11, 'fafdds')""")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
#
# db.commit()
#
# print  data

