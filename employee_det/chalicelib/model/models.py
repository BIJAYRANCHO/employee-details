from chalicelib.settings import DynaboDB
from chalicelib.model.config.oper import TableOper, TableOperExt

dynamoDb = DynaboDB.dynamoDb


class EmployeeDetails():
    def __init__(self): 
        self.tableName = 'employee_details'
        self.table = dynamoDb.Table(self.tableName)

    def is_idh_present(self):
        self.response = self.table.get_item(Key={'idh':self.idh, 'sort':self.sortKey}).get('Item')
        if self.response: return True
        else: return False

    def __call__(self, data): # for insert data into the table
        self.data = data
        self.idh = self.data.get('idh')
        self.sortKey = self.data.get('sort')
        self.is_idh = self.is_idh_present()
        if self.is_idh: return False
        self.table.put_item(Item=self.data)
        return True

    def get_object_by_key(self, idh, sortKey):
        self.idh = idh
        self.sortKey = sortKey
        self.object = TableOper(self.idh, self.table, self.sortKey)
        return self.object  

    def get_all_objects(self):
        self.object = TableOperExt(self.table) 
        return self.object

# class EmployeeLogin():
#     def __init__(self): 
#         self.tableName = 'employee_login'
#         self.table = dynamoDb.Table(self.tableName)

#     def is_idh_present(self):
#         self.response = self.table.get_item(Key={'idh':self.idh, 'sort':self.sortKey}).get('Item')
#         if self.response: return True
#         else: return False

#     def __call__(self, data): # for insert data into the table
#         self.data = data
#         self.idh = self.data.get('idh')
#         self.sortKey = self.data.get('sort')
#         self.is_idh = self.is_idh_present()
#         if self.is_idh: return False
#         self.table.put_item(Item=self.data)
#         return True

#     def get_object_by_key(self, idh, sortKey):
#         self.idh = idh
#         self.sortKey = sortKey
#         self.object = TableOper(self.idh, self.table, self.sortKey)
#         return self.object  

#     def get_all_objects(self):
#         self.object = TableOperExt(self.table) 
#         return self.object