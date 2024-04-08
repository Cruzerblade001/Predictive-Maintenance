import pandas as pd
#from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the dataset
data = pd.read_csv("ai4i2020.csv")
print(data.isnull().sum())

imputer = SimpleImputer(strategy='mean')
data[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']] = imputer.fit_transform(data[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']])

# data.drop(columns=['Type'], inplace=True)
new_data = data[data['Machine failure'] == 1]
print(new_data)
#print(data)

X = data.iloc[:,:-1].values

#print(X)

y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



random_forest_model = RandomForestClassifier()

random_forest_model.fit(X_train, y_train)

def evaluate_model(predictions, y_true):
    accuracy = accuracy_score(y_true, predictions)
    precision = precision_score(y_true, predictions)
    recall = recall_score(y_true, predictions)
    f1 = f1_score(y_true, predictions)
    roc_auc = roc_auc_score(y_true, predictions)
    return accuracy, precision, recall, f1, roc_auc

random_forest_predictions = random_forest_model.predict(X_test)

print("Random Forest:")
accuracy, precision, recall, f1, roc_auc = evaluate_model(random_forest_predictions, y_test)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("ROC AUC Score:", roc_auc)


joblib.dump(random_forest_model, 'trained_model.pkl')