import json

class return_func():
    def __call__(self):
        return {'msg':'hello_world'}

class jsonify():
    def __call__(self,**kwargs):
        return json.dumps(kwargs)