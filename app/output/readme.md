# IBM HR Analytics – Employee Attrition Prediction

## 📌 Project Overview

This project predicts whether an employee is likely to **leave the company (Attrition)** or **stay**, using machine learning models.
Employee attrition can lead to increased recruitment costs and productivity loss. This system helps HR teams identify employees who are at risk of leaving so that preventive actions can be taken.

---

## 🎯 Objective

The goal of this project is to build a **machine learning model** that analyzes employee data and predicts the probability of employee attrition.

---

## 📊 Dataset

Dataset used: **IBM HR Analytics Employee Attrition Dataset**

The dataset contains employee information such as:

* Age
* Gender
* Department
* Job Role
* Monthly Income
* Years at Company
* Job Satisfaction
* Work Life Balance
* Environment Satisfaction
* Performance Rating
* Overtime
* Attrition (Target variable)

Target variable:

* **Attrition = Yes → Employee leaves**
* **Attrition = No → Employee stays**

---

## 🧹 Data Preprocessing

### Handling Missing Values

Missing values were handled using **SimpleImputer**.

Strategies used:

* **Median** for numerical columns
* **Most Frequent** for categorical columns

### Feature Scaling

Numerical features were normalized using **StandardScaler** so that all features have similar scales.

### Encoding Categorical Variables

Categorical features were converted to numerical format using **OneHotEncoder**.

---

## ⚙️ Machine Learning Models

Two classification models were trained:

### 1. Logistic Regression

A statistical model used for **binary classification**.
It predicts the probability of an employee leaving using the **sigmoid function**.

### 2. Random Forest

An ensemble learning algorithm that builds multiple **decision trees** and combines their predictions using **majority voting**.

---

## 🔧 Model Optimization

### Pipeline

A **Pipeline** was used to combine preprocessing and model training steps.

Example:
Preprocessing → Model Training

### ColumnTransformer

Used to apply different preprocessing techniques to:

* Numerical features
* Categorical features

### Hyperparameter Tuning

**GridSearchCV** was used to find the best parameters for the models.

### Cross Validation

**StratifiedKFold** cross validation was used to maintain class balance during model training.

---

## 📈 Model Evaluation

Models were evaluated using:

* Accuracy
* ROC-AUC Score
* Confusion Matrix
* Precision
* Recall
* F1 Score

### Results Summary

Logistic Regression:

* Accuracy: **0.86**
* ROC-AUC: **0.81**

Confusion Matrix:
[[237 10]
[31 16]]

Random Forest:

* Accuracy: **0.85**
* ROC-AUC: **0.78**

Confusion Matrix:
[[244 3]
[41 6]]

Interpretation:
The confusion matrix shows correct and incorrect predictions made by the model for employees who stayed or left.

---

## 💾 Model Saving

The trained models were saved using **Joblib** so they can be reused without retraining.

Saved models:

* best_logistic.pkl
* best_rf.pkl

---

## 🌐 Web Application

A **Streamlit web application** was developed to allow users to input employee details and predict whether the employee is likely to leave or stay.

Users can enter details such as:

* Age
* Department
* Job Role
* Monthly Income
* Job Satisfaction
* Work Life Balance
* Years at Company

The system then predicts the **probability of employee attrition**.

---

## 🏗 Project Workflow

Dataset
↓
Data Preprocessing
↓
Feature Engineering
↓
Model Training
↓
Model Evaluation
↓
Model Saving
↓
Streamlit Deployment

---

## 💼 Business Impact

This system helps organizations:

* Identify employees at risk of leaving
* Reduce employee turnover
* Improve employee retention strategies
* Support HR decision-making

---

## 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## 📌 Conclusion

This project demonstrates how machine learning can be used to analyze employee data and predict attrition. Such systems help companies take proactive steps to improve employee satisfaction and retention.
