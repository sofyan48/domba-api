from flask import Blueprint
from flask_restful import Api
from .health import *
from .user import *
from .ttl import *


api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)

api.add_resource(HealthCheck, "/health")

api.add_resource(UserSignUp, "/user/add")
api.add_resource(GetUserData, "/user/list")
api.add_resource(GetUserDataId, "/user/list/<key>")
api.add_resource(UserUpdate, "/user/edit/<key>")
api.add_resource(UserDelete, "/user/delete/<key>")


api.add_resource(GetTtlData, "/ttl/list")
api.add_resource(GetTtlDataId, "/ttl/list/<key>")
api.add_resource(TtlAdd, "/ttl/add")
api.add_resource(TtlEdit, "/ttl/edit/<key>")
api.add_resource(TtlDelete, "/ttl/delete/<key>")