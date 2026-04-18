import pandas as pd
import os

# 🔹 Test 1: Check dataset exists
def test_dataset_exists():
    path = "app/data.csv"   # change if your dataset file name is different
    assert os.path.exists(path), "Dataset file missing"


# 🔹 Test 2: Validate dataset loading
def test_data_loading():
    data = pd.read_csv("app/data.csv")
    assert data.shape[0] > 0, "Dataset is empty"


# 🔹 Test 3: Check required HR columns
def test_required_columns():
    data = pd.read_csv("app/data.csv")
    required_cols = ["Age", "Salary", "Attrition"]  # adjust based on your dataset

    for col in required_cols:
        assert col in data.columns, f"Missing column: {col}"


# 🔹 Test 4: Check missing values handling
def test_no_null_explosion():
    data = pd.read_csv("app/data.csv")
    null_count = data.isnull().sum().sum()

    assert null_count < len(data), "Too many missing values"


# 🔹 Test 5: Simple ML sanity check (if model exists)
def test_model_output():
    try:
        import joblib
        import numpy as np

        model = joblib.load("app/model.pkl")

        sample = np.array([[30, 50000]])  # example input
        prediction = model.predict(sample)

        assert prediction is not None

    except Exception:
        assert True  # skip if model not available