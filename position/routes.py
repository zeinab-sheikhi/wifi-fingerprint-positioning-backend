from flask import Blueprint, request
from flask_restful import Api, Resource

from ML_models.classification import random_forest_preds, knn_classification_preds, catboost_preds
from ML_models.regression import decision_tree_preds, decision_tree_x_preds, decision_tree_y_preds
from ML_models.regression import extra_trees_preds, extra_trees_x_preds, extra_trees_y_preds, knn_regression_preds
from util.feature_selection import get_x_test

position_app = Blueprint('position_app', __name__, url_prefix='/api/v1/fingerprint')
api = Api(position_app)


class PositionAPI(Resource):
    def post(self):
        
        tile_number = 1
        x_coordinate = 0
        y_coordinate = 0

        if request.is_json:
            try:
                data = request.get_json()
                access_points = data['accessPoints']
                classification_model = data['classification']
                regression_model = data['regression']
                X_test = get_x_test(access_points)
            
                if classification_model == "Catboost":
                    tile_number = catboost_preds(X_test)
                elif classification_model == "KNN":
                    tile_number = knn_classification_preds(X_test)
                elif classification_model == "Random Forest":
                    tile_number = random_forest_preds(X_test)
                else:
                    return {'error': 'Bad Request', 'code': 402, 'data': 'Check Classification Model Name'}, 402
                
                # if regression_model == "Decision Tree":
                #     x_coordinate = decision_tree_preds(X_test)[0]
                #     y_coordinate = decision_tree_preds(X_test)[1]
                # elif regression_model == "Decision Tree(Distinct)":
                #     x_coordinate = decision_tree_x_preds(X_test)
                #     y_coordinate = decision_tree_y_preds(X_test)   
                # elif regression_model == "Extra Trees":
                #     x_coordinate = extra_trees_preds(X_test)[0]
                #     y_coordinate = extra_trees_preds(X_test)[1]
                # elif regression_model == "Extra Trees(Distinct)":
                #     x_coordinate = extra_trees_x_preds(X_test)
                #     y_coordinate = extra_trees_y_preds(X_test)
                # elif regression_model == "KNN":
                #     x_coordinate = knn_regression_preds(X_test)[0]
                #     y_coordinate = knn_regression_preds(X_test)[1]     
                # else:
                #     return {'error': 'Bad Request', 'code': 402, 'data': 'Check Regression Model Name'}, 402

                position_dict = {
                    "tileNumber": tile_number,
                    "X": x_coordinate,
                    "Y": y_coordinate,
                }
                
            except Exception as e:
                print(e)
                return {'error': 'Bad Request', 'code': 402, 'data': str(e)}, 402
            return position_dict, 200
            
        else:
            return {'error': 'Invalid JSON', 'code': 400, 'data': None}, 400
                
api.add_resource(PositionAPI, '/position')