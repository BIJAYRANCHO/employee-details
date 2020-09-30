import boto3, json

with open('chalicelib/model/config/table_org.json', 'r') as jsonRObj:
    table_det_dict = json.load(jsonRObj)

class DynaboDB():
    dynamoDb = boto3.resource('dynamodb')
   
    def __init__(self):
        self.dynamoDb = boto3.resource('dynamodb')

    def table_creation(self):
        self.table = self.dynamoDb.create_table(
        TableName=self.tableName,
        KeySchema=[
            {
                'AttributeName': self.partitionKey,
                'KeyType': self.partitionKeyType
            },
            {
                'AttributeName': self.sortKey,
                'KeyType': self.sortKeyType
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': self.partitionKey,
                'AttributeType': self.partitionKeyDef
            },
            {
                'AttributeName': self.sortKey,
                'AttributeType': self.sortKeyDef
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
        )
        return self.table.table_status

    def create_db(self):
        for table_name in list(table_det_dict.keys()):
            self.tableName = table_name
            self.partitionKey = table_det_dict.get(table_name).get('partitionKey')
            self.partitionKeyType = table_det_dict.get(table_name).get('partitionKeyType')
            self.partitionKeyDef = table_det_dict.get(table_name).get('partitionKeyDef')
            self.sortKey = table_det_dict.get(table_name).get('sortKey')
            self.sortKeyType = table_det_dict.get(table_name).get('sortKeyType')
            self.sortKeyDef = table_det_dict.get(table_name).get('sortKeyDef')
            self.table_status = self.table_creation()
            print (self.table_status+" => "+self.tableName)
        print ('\nDatabase created successfully!')