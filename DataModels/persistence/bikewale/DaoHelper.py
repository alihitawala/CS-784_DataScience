__author__ = 'aliHitawala'

class DaoHeper:
    def __init__(self):
        return

    _KeyToColumnNameForTemp = {
        'profile_id': 'id',
        'bike_name': 'bike_name',
        'city_posted': 'city_posted',
        'kilometer_done': 'km_driven',
        'color': 'color',
        'fuel_type': 'fuel_type',
        'price': 'price',
        'model_year': 'model_year',
        'owner_type': 'owner_type',
        'url': 'url'
    }
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
        list_ = []
        for key in dict:
            if self._KeyToColumnName.has_key(key):
                list_.append(self._KeyToColumnName[key])
            else :
                print "ERROR :: Couldn't locate column name for key = ", key, " URL = ", dict["URL"]
        return list_

    def getKeyToColumnNameForTemp(self, dictObj):
        list_ = []
        for key in dictObj:
            if key in self._KeyToColumnNameForTemp:
                list_.append(self._KeyToColumnNameForTemp[key])
            else :
                print "ERROR :: Couldn't locate column name for key = ", key, " URL = ", dictObj["url"]
        return list_
