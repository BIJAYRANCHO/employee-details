import json
from functools import wraps

class jsonify():
    def __call__(self, **kwargs):
        return json.dumps(kwargs)

class custom_checking():
    def check_employee_params(self, dict_data):
        self.dict_data = dict_data
        self.key_schema = ['firstname', 'lastname', 'mobile', 'password', 'email']
        self.dict_keys = list(self.dict_data.keys())
        for self.key in self.key_schema:
            if self.key not in self.dict_keys: return False 
        return True