import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamoDb = boto3.resource('dynamodb')


class EmployeeDetails():
    def __init__(self):
        self.tableName = 'employee_details'
        self.table = dynamoDb.Table(self.tableName)

    def __call__(self, data):
        self.data = data
        self.is_idh = self.is_idh_present(self.data.get('idh'))
        if self.is_idh: return False
        self.table.put_item(Item=self.data)
        return True

    def is_idh_present(self, idh):
        self.idh = idh
        self.response = self.table.get_item(Key={'idh':self.idh}).get('Item')
        if self.response: return True
        else: return False

    def fetch(self, idh):
        self.idh = idh
        self.response = self.table.get_item(Key={'idh':self.idh}).get('Item')
        return self.response

    def delete(self, idh):
        self.idh = idh
        self.key = {'idh': self.idh}
        outcome = self.table.delete_item(Key=self.key)
        return True

    def fetch_all(self):
        self.response = self.table.scan()
        self.items = self.response['Items']
        while 'LastEvaluatedKey' in self.response:
            print(self.response['LastEvaluatedKey'])
            response = self.table.scan(ExclusiveStartKey=self.response['LastEvaluatedKey'])
            self.items.extend(response['Items'])
        return self.items