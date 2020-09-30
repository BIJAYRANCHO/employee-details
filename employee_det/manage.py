import sys, os
from chalicelib import DynaboDB

class DBCreation():
    def __init__(self):
        self.outcome = DynaboDB.create_db()
        return self.outcome

class main():
    def __call__(self, cmd):
        self.cmd = cmd
        if self.cmd == 'create_db':
            createDB = DBCreation()
            return createDB

if __name__ == '__main__':
    main = main()
    try: cmd = sys.argv[1]
    except: 
        print ('no input detected!')
        os._exit(0)
    main(cmd)