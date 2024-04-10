# AI Maintenance Predictor

## Introduction
This project aims to predict maintenance requirements for manufacturing machines using machine learning techniques. It involves importing libraries, loading and preprocessing the dataset, model initialization and training, model evaluation, model persistence, visualization, taking input from Arduino, and displaying results on an LCD display.

## Importing Libraries
- **pandas:** Used for data manipulation and analysis.
- **scikit-learn:** Provides tools for machine learning tasks such as preprocessing, model building, and evaluation.
- **matplotlib:** A plotting library used for data visualization.
- **numpy:** Provides support for arrays, matrices, and mathematical functions.
- **joblib:** Used for saving and loading machine learning models.

## Loading the Dataset
The dataset named "ai4i2020.csv" is loaded using pandas' `read_csv()` function. This dataset likely contains information about manufacturing processes, including various features and a target variable.

## Data Preprocessing
Missing values in the dataset are handled using scikit-learn's `SimpleImputer` module with the strategy set to 'mean'. This replaces missing values with the mean of each respective column.

## Data Splitting
The dataset is split into features (X) and the target variable (y) using pandas' indexing. Further, the dataset is divided into training and testing sets using scikit-learn's `train_test_split()` function. This ensures that the model's performance can be evaluated on unseen data.

## Model Initialization and Training
Two classifiers are initialized: Logistic Regression and Random Forest, using their respective classes from scikit-learn. Both models are trained using the training data obtained in the previous step, by calling the `fit()` method on each model.

## Model Evaluation
Custom evaluation functions are defined to compute various performance metrics: accuracy, precision, recall, F1-score, and ROC AUC score. These functions use scikit-learn's metrics modules. Predictions are made on the test data using the trained models. The performance of each model is evaluated using the defined evaluation functions.

## Model Persistence
The trained Random Forest model is saved using joblib's `dump()` function. This allows for the model to be reused later without retraining.

## Visualization
A decision tree from the Random Forest model is visualized using scikit-learn's `plot_tree()` function. This provides insights into how the model makes decisions. A confusion matrix is plotted using matplotlib to visually represent the performance of the Random Forest model on the test data. This helps understand the model's performance in terms of true positives, true negatives, false positives, and false negatives.

## Taking Input from Arduino
Temperature data from Arduino Uno's internal temperature sensor is passed to Rpi through USB. Then the pkl file from the previous step is loaded and is fed the required data. The model then predicts whether the machine requires maintenance or whether the machine can continue its normal operation (no maintenance needed).

## Displaying Result on LCD Display
After predicting class either "1" (requires maintenance) or "0" (can continue its operation), it is sent to Arduino Uno. Depending upon the received class, Arduino displays on the LCD.

## How to Run the Project
1. Clone this repository to your local machine using `git clone <repository-url>`.
2. Install the required libraries using `pip install -r requirements.txt`.
3. To get address of Arduino when connected to raspberry pi. Type the command `ls/dev/tty*`. The option containing ACM will be your address.
4. Run the Hardware_project.py file to execute the project.
   
## Author
1. Harshit Sahu
2. Aditya 
3. Arpit Gandhi

## Video Link
https://youtu.be/t2JfOT9Hbh0



