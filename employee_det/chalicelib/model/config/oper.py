from boto3.dynamodb.conditions import Key, Attr


class TableOper():
    def __init__(self, idh, table):
        self.idh =idh
        self.table = table
    
    def is_idh_present(self):
        self.response = self.table.get_item(Key={'idh':self.idh}).get('Item')
        if self.response: return True
        else: return False

    def fetch_data(self):
        self.response = self.table.get_item(Key={'idh':self.idh}).get('Item')
        return self.response

    def delete(self):
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