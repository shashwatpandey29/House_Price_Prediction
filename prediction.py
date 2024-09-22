import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor
from flask import Flask, render_template, request

# Flask setup
app = Flask(__name__)

# Load and preprocess the dataset
dataset = pd.read_csv("HousePricePrediction.csv")

# Drop 'Id' column if it exists
if 'Id' in dataset.columns:
    dataset.drop(['Id'], axis=1, inplace=True)

# Fill missing target values
dataset['SalePrice'] = dataset['SalePrice'].fillna(dataset['SalePrice'].mean())

# Drop rows with missing values
new_dataset = dataset.dropna()

# Find categorical columns
categorical_cols = new_dataset.select_dtypes(include=['object']).columns

# Apply One-Hot Encoding
OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
OH_encoded_cols = pd.DataFrame(OH_encoder.fit_transform(new_dataset[categorical_cols]))
OH_encoded_cols.columns = OH_encoder.get_feature_names_out(categorical_cols)
OH_encoded_cols.index = new_dataset.index

# Drop original categorical columns and concatenate one-hot encoded columns
df_final = new_dataset.drop(categorical_cols, axis=1)
df_final = pd.concat([df_final, OH_encoded_cols], axis=1)

# Split the data
X = df_final.drop(['SalePrice'], axis=1)
Y = df_final['SalePrice']
X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)

# Train CatBoost Regressor (We'll use this for predictions)
model = CatBoostRegressor(verbose=0)
model.fit(X_train, Y_train)

# Function to make predictions from user input
def predict_price(input_data):
    # Convert input to DataFrame and ensure the same columns as training set
    input_df = pd.DataFrame([input_data], columns=X_train.columns)
    prediction = model.predict(input_df)
    return prediction[0]

# Flask route for the home page and prediction form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect form data
        input_data = {
            'MSSubClass': request.form['MSSubClass'],
            'LotArea': request.form['LotArea'],
            'OverallCond': request.form['OverallCond'],
            'YearBuilt': request.form['YearBuilt'],
            'YearRemodAdd': request.form['YearRemodAdd'],
            'BsmtFinSF2': request.form['BsmtFinSF2'],
            'TotalBsmtSF': request.form['TotalBsmtSF']
        }

        # Ensure proper numeric types for prediction
        input_data = {key: float(value) for key, value in input_data.items()}

        # Make a prediction
        predicted_price = predict_price(input_data)
        return render_template('dashboard.html', prediction=predicted_price)

    # For GET requests, just show the form
    return render_template('dashboard.html')

# Start Flask app
if __name__ == "__main__":
    app.run(debug=True)
