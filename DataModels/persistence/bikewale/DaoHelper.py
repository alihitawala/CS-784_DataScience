__author__ = 'aliHitawala'

class DaoHeper:
    def __init__(self):
        return

    _KeyToColumnName = {
        'Engine': 'engine',
        'City': 'city_posted',
        'Kms Done': 'kilometer_done',
        'Color': 'color',
        'BikeName': 'bike_name',
        'Profile Id': 'profile_id',
        'Seller': 'seller_type',
        'Fuel Type': 'fuel_type',
        'Asking Price (Rs.)': 'price',
        'Registration': 'city_registration',
        'Owner': 'owner_type',
        'Model Year': 'model_year',
        'Insurance': 'insurance',
        'Lifetime-Tax': 'lifetime_tax_type',
        'URL': 'url',
        'StateCode': 'state_code'
    }

    def getKeyToColumnName (self, dict):
        list = []
        for key in dict:
            if self._KeyToColumnName.has_key(key):
                list.append(self._KeyToColumnName[key])
            else :
                print "ERROR :: Couldn't locate column name for key = ", key, " URL = ", dict["URL"]
        return list
