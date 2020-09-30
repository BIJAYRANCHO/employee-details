from chalicelib.extension import jsonify
from chalicelib.model import *
from hashlib import md5

class RestViewIndex():
    def __init__(self):
        self.name = 'Aniket_Sarkar'

    def index(self):
        return jsonify(msg='This is the index page.', resp_code='tip', status_code=200)


class RestViewEmployee():
    def __init__(self):
        self.name = 'Aniket_Sarkar'

    def collect(self, reqMethod, reqBody):
        self.reqMethod = reqMethod
        self.reqBody = reqBody

    def make_requestBody(self):
        self.idh = md5(self.reqBody.get('email').encode('utf-8')).hexdigest()
        self.sort = md5(self.reqBody.get('mobile').encode('utf-8')).hexdigest()
        self.reqBody.update({'idh':self.idh, 'sort':self.sort})
        return self.reqBody

    def employee(self, reqMethod, reqBody):
        self.collect(reqMethod, reqBody)
        if self.reqMethod == 'PUT':
            self.reqBody = self.make_requestBody()
            self.insert_resp = EmployeeDetails(self.reqBody)
            if not self.insert_resp: return jsonify(msg='email already present', resp_code='eap', status_code=403)
            else: return jsonify(msg='employee inserted successfully', email= self.reqBody.get('email'))
        if self.reqMethod == 'POST':
            self.reqBody = self.make_requestBody()
            EmployeeObj = EmployeeDetails.get_object_by_key(self.reqBody.get('idh'), self.reqBody.get('sort'))
            employee_det = EmployeeObj.fetch_data()
            return employee_det
        if self.reqMethod == 'DELETE':
            self.reqBody = self.make_requestBody()
            EmployeeObj = EmployeeDetails.get_object_by_key(self.reqBody.get('idh'), self.reqBody.get('sort'))
            employee_delete = EmployeeObj.delete()
            if not employee_delete: return jsonify(msg='failed to delete employee', resp_code='fde', status_code=403)
            else: return jsonify(msg='employee %s deleted successfully'%self.reqBody.get('email'), resp_code='eds', status_code=200)
        if self.reqMethod == 'GET':
            EmployeeObj = EmployeeDetails.get_all_objects()
            return EmployeeObj.fetch_all()