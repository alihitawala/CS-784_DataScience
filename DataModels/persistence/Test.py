from DataModels.persistence.DBConnector import Connector

__author__ = 'shaleen'


db = Connector().generateDBConnector('TEST')

# prepare a cursor object using cursor() method
cursor =  db.cursor()

# execute SQL query using execute() method.
cursor.execute("""INSERT INTO `test`.`new_table` (`id`, `test`) VALUES (15, 'fafdds')""")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

db.commit()

print  data