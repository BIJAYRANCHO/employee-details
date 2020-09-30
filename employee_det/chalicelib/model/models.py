import boto3
from chalicelib.settings import DynaboDB
from chalicelib.model.config.oper import TableOper

dynamoDb = DynaboDB.dynamoDb

class EmployeeDetails():
    def __init__(self): 
        self.tableName = 'employee_details'
        self.table = dynamoDb.Table(self.tableName)

    def __call__(self, data): # for insert data into the table
        self.data = data
        self.is_idh = self.is_idh_present(self.data.get('idh'))
        if self.is_idh: return False
        self.table.put_item(Item=self.data)
        return True

    def get_object_by_idh(self, idh):
        self.idh = idh
        self.object = TableOper(self.idh, self.table)
        return self.object   