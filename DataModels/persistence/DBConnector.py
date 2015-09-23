__author__ = 'shaleen'

import MySQLdb
import abc

class Connector:

    QUICKRDB = 'test'
    QUICKRROOT = 'root'
    QUICKRPASS = 'help2012'
    QUICKRLOCAL = 'localhost'
    QUICKRTABLE = 'Quickr'

    TESTDB = 'test'
    TESTROOT = 'root'
    TESTPASS = 'hussain'
    TESTLOCAL = 'localhost'
    TESTTABLE = 'new_table'

    BIKEWALEDB = 'test'
    BIKEWALEROOT = 'root'
    BIKEWALEPASS = 'hussain'
    BIKEWALELOCAL = 'localhost'
    BIKEWALETABLE = 'Bikewale'


    def generateDBConnector(self, root):
        if root == 'QUICKR':
            return MySQLdb.connect(self.QUICKRLOCAL, self.QUICKRROOT, self.QUICKRPASS, self.QUICKRDB)
        if root == 'BIKEWALE':
            return MySQLdb.connect(self.BIKEWALELOCAL, self.BIKEWALEROOT, self.BIKEWALEPASS, self.BIKEWALEDB)
        if root == 'TEST':
            return MySQLdb.connect(self.QUICKRLOCAL, self.QUICKRROOT, self.QUICKRPASS, self.QUICKRDB)

    @abc.abstractmethod
    def getCursor(self):
        return

    @abc.abstractmethod
    def getInsertQueryTemplate(self, obj):
        return

    @abc.abstractmethod
    def populateAndExecute(self, obj):
        return


