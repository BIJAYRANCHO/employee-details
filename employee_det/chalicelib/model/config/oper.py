from boto3.dynamodb.conditions import Key, Attr


class TableOper():
    def __init__(self, idh, table, sortKey):
        self.idh =idh
        self.table = table
        self.sortKey = sortKey

    def fetch_one(self):
        self.response = self.table.get_item(Key={'idh': self.idh, 'sort': self.sortKey}).get('Item')
        return self.response

    def delete(self):
        self.key = {'idh': self.idh, 'sort': self.sortKey}
        outcome = self.table.delete_item(Key=self.key)
        return True


class TableOperExt():
    def __init__(self, table):
        self.table = table

    def fetch_all(self):
        self.response = self.table.scan()
        self.items = self.response['Items']
        while 'LastEvaluatedKey' in self.response:
            response = self.table.scan(ExclusiveStartKey=self.response['LastEvaluatedKey'])
            self.items.extend(response['Items'])
        return self.items
