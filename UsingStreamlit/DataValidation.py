import pandas as pd
def isDataValidate(data: dict):
    try:
        required_fields = ['gender', 'tenure', 'MonthlyCharges', 'TotalCharges']
        for field in required_fields:
            if field not in data or data[field] is None:
                return False, f"Missing required field: {field}"
        if data['tenure'] < 0 or data['tenure'] >72:
            return False, f'Tenure should be between 0 to 72'
        if data['tenure'] <=0 or data['MonthlyCharges'] <= 0:
            return False, "Tenure and MonthlyCaharges should be greater than 0"
        if data['tenure'] * data['MonthlyCharges'] > data['TotalCharges']:
            return False, "Tenure into MonthlyCharges should not be grater than TotalCharges"
        return True,' Data is valid'
    except Exception as e:
        print(e)
        return False, 'Something went wrong during data validation'
