from chalice import Chalice
import boto3
import json
import hashlib
from chalicelib import *
from chalicelib.model import *
from chalicelib.router import *

app = Chalice(app_name='employee_det')
app.register_blueprint(BlueprintRegister.router)
app.api.cors = True
app.debug = True

#app.register_blueprint(router)

# @app.route('/')
# def index():
#     return jsonify(msg='This is the index page.', resp_code='tip', status_code=200)

@app.route('/add-employee', methods=['POST'])
def add_employee():
    employeeData = app.current_request.json_body
    id_hash = hashlib.md5(employeeData.get('email').encode('utf-8')).hexdigest()
    employeeData.update({'idh':id_hash})
    insert_resp = EmployeeDetails(employeeData)
    if not insert_resp: return jsonify(msg='email already present', resp_code='eap', status_code=403)
    else: return jsonify(msg='employee inserted successfully', email= employeeData.get('email'))

@app.route('/get-employee-details', methods=['POST'])
def get_employee_details():
    employeeData = app.current_request.json_body
    id_hash = hashlib.md5(employeeData.get('email').encode('utf-8')).hexdigest()
    Employee = EmployeeDetails.get_object_by_idh(id_hash)
    employee_det = Employee.fetch_data()
    return employee_det

@app.route('/delete-employee', methods=['DELETE'])
def delete_employee():
    employeeData = app.current_request.json_body
    id_hash = hashlib.md5(employeeData.get('email').encode('utf-8')).hexdigest()
    delete_resp = EmployeeDetails.delete(id_hash)
    return jsonify(msg='employee record deleted successfully', resp_code='eds', status_code=200)

@app.route('/get-all-employees', methods=['GET'])
def get_all_employees():
    return EmployeeDetails.fetch_all()
