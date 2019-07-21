from flask_restful import Resource, reqparse
from app.helpers.rest import response
from app.models import model
from app.libs import utils
from app.libs import validation


class GetDomainData(Resource):
    def get(self):
        results = list()
        try:
            data_zone = model.read_all("zone")
        except Exception as e:
            return response(401, message=str(e))
        
        for i in data_zone:
            user = model.read_by_id("user", i['user'])
            record = model.record_by_zone(i['key'])
            data = {
                "key": i['key'],
                "value": i['value'],
                "created_at": i['created_at'],
                "user": user,
                "record": record
            }
            results.append(data)
        return response(200, data=results)


class GetDomainDataId(Resource):
    def get(self, key):
        try:
            data_zone = model.read_by_id("zone", key)
        except Exception as e:
            return response(401, message=str(e))
        else:
            user = model.read_by_id("user", data_zone['user'])
            record = model.record_by_zone(data_zone['key'])
            data = {
                "key": data_zone['key'],
                "value": data_zone['value'],
                "created_at": data_zone['created_at'],
                "user": user,
                "record": record
            }
            return response(200, data=data)


class DeleteDomain(Resource):
    def delete(self, key):
        try:
            record = model.record_by_zone(key)
        except Exception as e:
            return response(401, message="Record Not Found | "+str(e))
        else:
            for i in record:
                try:
                    model.record_delete(i['key'])
                except Exception as e:
                    print(e)
        try:
            model.delete("zone", key)
        except Exception as e:
            return response(401, message=str(e))
        else:
            return response(200, message="Domain Or Zone Deleted")