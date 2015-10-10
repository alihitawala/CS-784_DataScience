__author__ = 'aliHitawala'
from DataModels.persistence.bikewale.BikeWaleDaoImpl import Dao
import re

def tranfer_data_from_stage_to_temp():
    dao = Dao()
    rows = dao.get_entries_from_stage()
    for row in rows:
        for key in row:
            row[key] = row[key].strip()
            if key == 'kilometer_done' or key == 'price':
                row[key] = int(row[key].replace(',', ''))
            elif key == 'model_year':
                row[key] = int(re.search(r'([A-Za-z]{3})(-)(.+\d)', row[key]).group(3))
            elif key == 'profile_id':
                row[key] = int(re.search(r'(S)(.+\d)', row[key]).group(2))
        dao.populateAndExecuteIntoTemp(row)


tranfer_data_from_stage_to_temp()