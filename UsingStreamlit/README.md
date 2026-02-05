# Customer Churn Prediction - Streamlit Application

A web-based customer churn prediction application built with Streamlit that uses a pre-trained Logistic Regression model to predict whether a telecom customer is likely to churn.

## 📋 Overview

This Streamlit application provides an interactive interface for predicting customer churn based on various customer attributes such as demographics, services subscribed, contract details, and billing information. The model was trained in Google Colab using the Telco Customer Churn dataset and saved using pickle for deployment.

## 🚀 Features

- **Interactive UI**: User-friendly interface with radio buttons, sliders, and input fields
- **Real-time Validation**: Validates user input before making predictions
- **Logistic Regression Model**: Pre-trained model loaded via pickle
- **Comprehensive Input Fields**: Collects 19 different customer attributes
- **Error Handling**: Robust error handling for model loading and predictions

## 📁 Project Structure

```
UsingStreamlit/
├── main.py                              # Main Streamlit application
├── PredictionModel.py                   # Model loading and prediction logic
├── DataValidation.py                    # Input data validation
├── LogisticRegressionChurnModel.pkl     # Pre-trained model file
├── pyproject.toml                       # Project dependencies
├── uv.lock                              # Dependency lock file
├── .python-version                      # Python version specification (3.12)
└── README.md                            # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.12 or higher
- uv package manager (or pip)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/parmindersarao/CustomerChurnPredictionProject.git
cd CustomerChurnPredictionProject/UsingStreamlit
```

2. Install dependencies using uv:
```bash
uv sync
```

## 🎯 Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 🔍 Data Validation

The application includes robust data validation (`DataValidation.py`) that checks:

- ✅ All required fields are present (gender, tenure, MonthlyCharges, TotalCharges)
- ✅ Tenure is between 0 and 72 months
- ✅ Tenure and Monthly Charges are greater than 0
- ✅ Total Charges is logically consistent (not less than tenure × monthly charges)

## 🤖 Model Information

- **Model Type**: Logistic Regression
- **Training**: Model was trained in Google Colab using the Telco Customer Churn dataset
- **Serialization**: Saved using Python's pickle module
- **Output**: 
  - Binary prediction (Churn: Yes/No)
  - Probability scores for both classes

## 📦 Dependencies

```toml
[project]
requires-python = ">=3.12"
dependencies = [
    "scikit-learn>=1.6.0<1.7.0",
    "streamlit>=1.53.1",
]
```

## 🔧 Code Components

### main.py
The main application file that creates the Streamlit interface with:
- Two-column layout for organized input fields
- Submit button for making predictions
- Integration with validation and prediction modules

### PredictionModel.py
Handles model operations:
- `LoadModel()`: Loads the pickled Logistic Regression model
- `PredictChurn(data)`: Makes predictions on input data
- Error handling for missing model files

### DataValidation.py
Validates user input:
- `isDataValidate(data)`: Checks data integrity and business logic
- Returns validation status and error messages

## 🐛 Error Handling

The application handles various error scenarios:
- Missing model file
- Invalid input data
- Model loading errors
- Prediction errors

## 🚧 Future Enhancements

- FastAPI implementation (mentioned in main repository description)
- Model performance metrics display
- Feature importance visualization
- Export predictions to CSV
- Multi-model comparison

## 👤 Author

**Parminder Sarao**

## 📝 License

This project is part of the CustomerChurnPredictionProject repository.

## 🔗 Related Files

- Training Notebook: `Customer_churn_prediction.ipynb` (in parent directory)
- Dataset: `Telco-Customer-Churn.csv` (in parent directory)

---

For more information about the model training process, refer to the Jupyter notebook in the main repository directory.
