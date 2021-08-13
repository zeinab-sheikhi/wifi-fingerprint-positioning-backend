from util.feature_selection import open_pkl_file, open_joblib_file
from util.string_utils import StringUtils

def decision_tree_preds(X_test):
    
    extra_trees_model = open_pkl_file('../trained_models/regression/decision_tree_model.pkl')
    extra_trees_preds = extra_trees_model.predict(X_test).tolist()[0]
    return extra_trees_preds

def decision_tree_x_preds(X_test):
    
    extra_trees_model = open_pkl_file('../trained_models/regression/decision_tree_x_model.pkl')
    extra_trees_preds = extra_trees_model.predict(X_test).tolist()[0]
    return extra_trees_preds

def decision_tree_y_preds(X_test):
    
    extra_trees_model = open_pkl_file('../trained_models/regression/decision_tree_y_model.pkl')
    extra_trees_preds = extra_trees_model.predict(X_test).tolist()[0]
    return extra_trees_preds

def extra_trees_preds(X_test):
    
    # extra_trees_model = open_joblib_file(StringUtils.mean_imputation_regression_model_path)
    # extra_trees_model = open_joblib_file(StringUtils.min_imputation_regression_model_path)
    extra_trees_model = open_joblib_file(StringUtils.zero_imputation_regression_model_path)
    extra_trees_preds = extra_trees_model.predict(X_test).tolist()[0]
    return extra_trees_preds

def extra_trees_x_preds(X_test):
    
    # extra_trees_x_model = open_joblib_file(StringUtils.mean_imputation_regression_x_model_path)
    extra_trees_x_model = open_joblib_file(StringUtils.min_imputation_regression_x_model_path)
    # extra_trees_x_model = open_joblib_file(StringUtils.zero_imputation_regression_x_model_path)
    extra_trees_x_preds = extra_trees_x_model.predict(X_test).tolist()[0]
    return extra_trees_x_preds

def extra_trees_y_preds(X_test):
    
    # extra_trees_y_model = open_joblib_file(StringUtils.mean_imputation_regression_y_model_path)
    extra_trees_y_model = open_joblib_file(StringUtils.min_imputation_regression_y_model_path)
    # extra_trees_y_model = open_joblib_file(StringUtils.zero_imputation_regression_y_model_path)
    extra_trees_y_preds = extra_trees_y_model.predict(X_test).tolist()[0]
    return extra_trees_y_preds

def knn_regression_preds(X_test):

    knn_model = open_pkl_file('../trained_models/regression/knn_model.pkl')
    knn_preds = knn_model.predict(X_test).tolist()[0]
    return knn_preds
