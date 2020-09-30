from chalice import Chalice
from chalicelib.router import *

app = Chalice(app_name='employee_det')
app.register_blueprint(BlueprintRegister.router)
app.api.cors = True
app.debug = True