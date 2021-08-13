from util.feature_selection import open_pkl_file, open_joblib_file
from util.string_utils import StringUtils

def catboost_preds(X_test):

    catboost_model = open_pkl_file(StringUtils.zero_imputation_classification_model_path)
    catboost_preds = catboost_model.predict(X_test).tolist()[0][0]
    return catboost_preds

def knn_classification_preds(X_test):

    knn_model = open_joblib_file(StringUtils.zero_imputation_classification_model_path)
    knn_preds = knn_model.predict(X_test).tolist()[0]
    return knn_preds

def random_forest_preds(X_test):
    
    # random_forest_model = open_joblib_file(StringUtils.mean_imputation_classification_model_path)
    # random_forest_model = open_joblib_file(StringUtils.min_imputation_classification_model_path)
    random_forest_model = open_joblib_file(StringUtils.zero_imputation_classification_model_path)
    random_forest_preds = random_forest_model.predict(X_test).tolist()[0]
    return random_forest_preds
