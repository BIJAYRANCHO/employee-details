from chalice import Blueprint
from chalicelib.views import *
from chalicelib.extension import custom_checking

class BlueprintRegister():
    def __init__(self):
        self.router = Blueprint(__name__)

class RouteMakerIndex():
    def __call__(self):
        self.router = BlueprintRegister.router
        @self.router.route('/')
        def index():
            return RestViewIndex.index()
        
class RouteMakerEmployee():
    def __call__(self):
        self.router = BlueprintRegister.router
        @self.router.route('/employee', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
        def employee():
            self.request_method = self.router.current_request.method
            self.request_body = self.router.current_request.json_body
            return RestViewEmployee.employee(self.request_method, self.request_body)











BlueprintRegister=BlueprintRegister()