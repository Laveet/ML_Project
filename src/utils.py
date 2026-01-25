import sys
import os
import pandas as pd
import numpy as np
from src.loger import logging
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(path,obj):
    try:
        dir_path=os.path.dirname(path)
        os.makedirs(dir_path,exist_ok=True)

        with open(path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(sys,e)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:

        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            # parameters=params[list(params.keys())[i]]
            # gs=GridSearchCV(model,parameters,cv=3)
            # gs.fit(X_train,y_train)
            # model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
        return report
    except Exception as e:
        raise CustomException(e,sys)
        
    
        
