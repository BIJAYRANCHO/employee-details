from chalicelib.extension import *
from chalicelib.model import *
from hashlib import md5, sha256

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
        if not custom_checking.check_employee_params(self.reqBody): return jsonify(msg= 'missing parameter value/values', resp_code= 'mpv', status_code= 422)
        if self.reqMethod == 'PUT': # for signup 
            self.password_hash = sha256(self.reqBody.get('password').encode('utf-8')).hexdigest()
            self.reqBody.update({'password': self.password_hash})
            self.reqBody = self.make_requestBody()
            self.insert_resp = EmployeeDetails(self.reqBody)
            if not self.insert_resp: return jsonify(msg='email already present', resp_code='eap', status_code=403)
            else: return jsonify(msg='employee inserted successfully', email= self.reqBody.get('email'), resp_code='eis', status_code=200)
        if self.reqMethod == 'POST': # for fetching single employee data
            self.reqBody = self.make_requestBody()
            self.EmployeeObj = EmployeeDetails.get_object_by_key(self.reqBody.get('idh'), self.reqBody.get('sort'))
            self.employee_det = self.EmployeeObj.fetch_one()
            return self.employee_det
        if self.reqMethod == 'DELETE': # delete a employee
            self.reqBody = self.make_requestBody()
            self.EmployeeObj = EmployeeDetails.get_object_by_key(self.reqBody.get('idh'), self.reqBody.get('sort'))
            self.employee_delete = self.EmployeeObj.delete()
            if not self.employee_delete: return jsonify(msg='failed to delete employee', resp_code='fde', status_code=403)
            else: return jsonify(msg='employee %s deleted successfully'%self.reqBody.get('email'), resp_code='eds', status_code=200)
        if self.reqMethod == 'GET': # get all employee record
            self.EmployeeObj = EmployeeDetails.get_all_objects()
            return self.EmployeeObj.fetch_all()
        if self.reqMethod == 'OPTIONS': # using for login purpose
            self.reqBody = self.make_requestBody()
            self.EmployeeObj = EmployeeDetails.get_object_by_key(self.reqBody.get('idh'), self.reqBody.get('sort'))
            self.employee_det = self.EmployeeObj.fetch_one()
            self.dbPassword = self.employee_det.get('password')
            self.recvPasswordHash = sha256(self.reqBody.get('password').encode('utf-8')).hexdigest()
            if not self.dbPassword == self.recvPasswordHash: return jsonify(msg='credential mismatched', resp_code='cmm', status_code=403)
            else: return jsonify(msg='employee login successful', resp_code='els', status_code=200)


    # def employee_login(self, reqMethod, reqBody):
    #     self.collect(reqMethod, reqBody)
    #     if self.reqMethod == 'POST':
    #         self.reqBody = self.make_requestBody()
