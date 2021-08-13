from flask import Blueprint, request
from flask_restful import Api, Resource

from models import Point, AccessPoint
from database.db import db_session

point_app = Blueprint('point_app', __name__, url_prefix='/api/v1/fingerprint')
api = Api(point_app)


class PointAPI(Resource):

    # def get(self):
    #     message = {'data': 'x,y values changed successfully!', 'error': '', 'code': 200}
    #     x_instance = db_session.query(Point).filter(Point.x != 0).all()
    #     for row in x_instance:
    #         current_x = row.xe
    #         counter  = current_x // 40 
    #         new_x = current_x + 20 * counter
    #         print(new_x)
    #         row.x = new_x
    #     db_session.commit()    
    #     y_instance = db_session.query(Point).filter(Point.y != 0).all()
    #     for row in y_instance:
    #         current_y = row.y
    #         counter  = current_y // 40 
    #         new_y = current_y + 20 * counter
    #         print(new_y)
    #         row.y = new_y    
    #     db_session.commit()    
    #     return message

    def post(self):
        if request.is_json:
            try:
                data = request.get_json()
                x = data['x']
                y = data['y']
                total_scan_time = data['T']
                interval_time = data['Ts']
                date_time = data['dateTime']
                accessPoints = data['accessPoints']

                new_point = Point(x, y, total_scan_time, interval_time, date_time)
                db_session.add(new_point)
                db_session.commit()

                for ap in accessPoints:
                    vals = list(ap.values())
                    bssid = vals[0]
                    rssi_list = vals[1]
                    new_access_point = AccessPoint(new_point.id, bssid, rssi_list)
                    db_session.add(new_access_point)
                    db_session.commit()

            except Exception as e:
                return {'error': 'Bad Request', 'code': 402, 'data': {}}, 402

            return {'error': '', 'code': 200, 'data': f"Point has been saved on ({new_point.x},{new_point.y})"}

        else:
            return {'error': 'Invalid JSON', 'code': 400, 'data': {}}, 400              
api.add_resource(PointAPI, '/points')