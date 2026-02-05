import pickle
import pandas as pd
import os


def LoadModel():
    try:
        path = os.path.join(os.path.dirname(__file__), 'LogisticRegressionChurnModel.pkl')
        Model= pickle.load(open(path,'rb'))
        return Model
    except FileNotFoundError:
        return 'Model file not found.'
    except Exception as e:
        return f'Error Loading Model: {e}'
def PredictChurn(data: pd.DataFrame):
    try:
        Model=LoadModel()
        if isinstance(Model, str):
            return Model
        result = [Model.predict(data),Model.predict_proba(data)]
        return result
    except Exception as e:
        return f'Error during prediction: {e}'
    
Model=LoadModel()
if isinstance(Model, str):
    print(Model)
else:
    print('Model Loaded Successfully')