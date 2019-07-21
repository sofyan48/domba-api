from flask import Blueprint
from flask_restful import Api
from .health import *
from .user import *
from .ttl import *
from .type import *
from .zone import *
from .record import *


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


api.add_resource(GetTypeData, "/type/list")
api.add_resource(GetTypeDataId, "/type/list/<key>")
api.add_resource(TypeAdd, "/type/add")
api.add_resource(TypeEdit, "/type/edit/<key>")
api.add_resource(TypeDelete, "/type/delete/<key>")


api.add_resource(GetZoneData, "/zone/list")
api.add_resource(GetZoneDataId, "/zone/list/<key>")
api.add_resource(ZoneAdd, "/zone/add")
api.add_resource(ZoneEdit, "/zone/edit/<key>")
api.add_resource(ZoneDelete, "/zone/delete/<key>")

api.add_resource(GetRecordData, "/record/list")
api.add_resource(GetRecordDataId, "/record/list/<key>")
api.add_resource(RecordAdd, "/record/add")
api.add_resource(RecordEdit, "/record/edit/<key>")
api.add_resource(RecordDelete, "/record/delete/<key>")
