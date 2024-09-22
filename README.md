# 🏠 House Price Prediction using Machine Learning 🧠

Welcome to the **House Price Prediction** project! This project leverages machine learning algorithms to predict house prices based on various features from a dataset. It includes a simple web-based interface using Flask, allowing users to input house details and receive predictions.

## 📚 Table of Contents
- [Introduction](#-introduction)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Models Used](#-models-used)
- [Evaluation](#-evaluation)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Introduction
Buying a house is one of the biggest investments, and predicting house prices accurately can greatly assist buyers and sellers. This project builds models to predict house prices using a dataset that includes multiple features such as lot area, year built, basement area, and more. The model's performance is evaluated using various metrics such as Mean Squared Error (MSE) and R-squared (R²).

## 📊 Dataset
The dataset contains several features used to predict the house sale price, including:
1. **MSSubClass**: Type of dwelling (e.g., Single-family, duplex).
2. **LotArea**: Lot size in square feet.
3. **OverallCond**: Overall condition of the house (rating).
4. **YearBuilt**: Year the house was originally built.
5. **YearRemodAdd**: Year of last remodeling.
6. **BsmtFinSF2**: Finished square footage of the basement.
7. **TotalBsmtSF**: Total square footage of the basement.
8. **SalePrice**: Sale price of the house (target variable).

![Dataset Overview](https://media.istockphoto.com/id/1567429058/photo/landscaping-on-middleclass-homes-aerial-neighborhood-fresh-cut-lawns.jpg?s=2048x2048&w=is&k=20&c=-RSlRMjm0s6vhmHdNOBoVS-J4nuJWdmaSHXK1_ErpVU=)

## ⚙️ Installation
To get the project up and running on your local machine, follow the instructions below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Elangovan0101/House-price-prediction.git
    cd House-price-prediction
    ```

2. **Install dependencies**:
    Ensure you have Python installed. Then, install the required packages using:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage
After the installation, you can run the Flask app and use the web interface to make predictions.

1. **Run the Flask app**:
    ```bash
    python app.py
    ```

2. **Navigate to the web interface**:
   - Open your browser and go to `http://127.0.0.1:5000/`
   - Enter house details in the form and click "Predict" to see the predicted house price.

## 🤖 Models Used
The following machine learning models are trained on the dataset:
1. **Support Vector Machine (SVM)**: A regression model that works well for small datasets.
2. **Random Forest Regressor**: An ensemble method that fits multiple decision trees and averages the results for better accuracy.
3. **Linear Regression**: A simple regression model for predicting continuous values.
4. **CatBoost Regressor**: A high-performance boosting model specifically designed for categorical data.

## 📈 Evaluation
The models are evaluated based on:
- **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
- **R-squared (R²)**: Indicates the proportion of the variance in the target variable that the model can explain.

## 🤝 Contributing
Contributions are welcome! If you want to contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Open a pull request.

## 📝 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

