import streamlit as st
import pandas as pd
import DataValidation
import PredictionModel
def main():
    st.title("Cutomer Churn Prediction App")
    st.write("Enter data as requested below:")
    col1, col2= st.columns(2)
    with col1:
        gender = st.radio('Gender',['Male','Female'])
        SeniorCitizen = st.radio('Are you a Senior Citizen?',('Yes','No'))
        Partner = st.radio('Do you have a Partner?',('Yes','No'))
        Dependents = st.radio('Do you have Dependents?',('Yes','No'))
        TechSupport = st.radio('Do you have Tech Support?',('Yes','No','No internet service'))
        StreamingTV = st.radio('Do you have Streaming TV?',('Yes','No','No internet service'))
        StreamingMovies = st.radio('Do you have Streaming Movies?',('Yes','No','No internet service'))
    with col2:
        tenure = st.slider('Tenure (in months)',0,72,1)
        PhoneService = st.radio('Do you have Phone Service?',('Yes','No','No Phone Service'))
        MultipleLines = st.radio('Do you have Multiple Lines?',('Yes','No'))
        OnlineSecurity = st.radio('Do you have Online Security?',('Yes','No','No internet service'))
        OnlineBackup = st.radio('Do you have Online Backup?',('Yes','No','No internet service'))
        DeviceProtection = st.radio('Do you have Device Protection?',('Yes','No','No internet service'))
        PaperlessBilling = st.radio('Do you have Paperless Billing?',('Yes','No'))
    InternetService = st.selectbox('Internet Service Type',['DSL','Fiber optic','No'])
    Contract = st.selectbox('Contract Type',['Month-to-month','One year','Two year'])
    PaymentMethod = st.selectbox('Payment Method',['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    MonthlyCharges = st.number_input('Monthly Charges',0.0,1000.0)
    TotalCharges = st.number_input('Total Charges',0.0,10000.0)
    Input_Data = {'gender':gender,
                  'SeniorCitizen':1 if SeniorCitizen=='Yes' else 0,
                  'Partner':Partner,
                  'Dependents':Dependents,
                  'tenure':tenure,
                  'PhoneService' :PhoneService,
                  'MultipleLines':MultipleLines,
                  'InternetService':InternetService,
                  'OnlineSecurity':OnlineSecurity,
                  'OnlineBackup':OnlineBackup,
                  'DeviceProtection': DeviceProtection,
                  'TechSupport' : TechSupport,
                  'StreamingTV' :StreamingTV,
                  'StreamingMovies' :StreamingMovies,
                  'Contract' :Contract,
                  'PaperlessBilling' :PaperlessBilling,
                  'PaymentMethod' : PaymentMethod,
                  'MonthlyCharges' : MonthlyCharges,
                  'TotalCharges' : TotalCharges}

    if st.button('Submit'):
        print(type(Input_Data))
        print(Input_Data)
        isDataValidate, errorMessage = DataValidation.isDataValidate(Input_Data)
        if not isDataValidate:
            print(errorMessage)
            st.popover(errorMessage)
        else:
            Input_Data=pd.DataFrame([Input_Data])
            st.popover('Data Validate Succesfuly')
            result= PredictionModel.PredictChurn(Input_Data)
            if isinstance(result, str):
                st.error(result)
            else:
                st.write(f'The model predicts that the customer is likely to churn:')  
                if result[0]:
                    st.error(f'The customer is likely to churn with a probability of {result[1][0][1]:.2%}.')
                else:
                    st.success(f'The customer is unlikely to churn with a probability of {result[1][0][0]:.2%}.')


    


if __name__ == "__main__":
    main()
