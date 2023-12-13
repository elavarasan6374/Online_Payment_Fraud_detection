# -*- coding: utf-8 -*-
"""Online_Payment_Fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rEABSLVOFpo6_dqTa-eOGmkHsCPw1frh
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

data = pd.read_csv('/content/drive/MyDrive/Machine_learning/Online_Payment_Fraud_Detction.csv')

print(data)

for i in data.columns:
  print(i)

data.head()

data.tail()

data.shape

data.describe()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
# Drop irrelevant columns
data = data.drop(columns=['nameOrig', 'nameDest', 'isFlaggedFraud'])

# Compute the correlation matrix
correlation_matrix = data.corr()

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

import matplotlib.pyplot as plt
plt.hist(data['isFraud'], bins=5, edgecolor='black')
plt.title(f'Distribution of isFraud')
plt.xlabel('isFraud')
plt.ylabel('Frequency')
plt.show()

# Create a stacked bar plot
plt.figure(figsize=(10, 6))
sns.countplot(x='type', hue='isFraud', data=data)
plt.title('Transaction Type vs. Fraud Status')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.show()

data = pd.get_dummies(data = data,columns = ['type'], drop_first = True)
data.head()

from sklearn.preprocessing import RobustScaler
rscaler = RobustScaler()
scaled_data = rscaler.fit_transform(data)
data = pd.DataFrame(scaled_data, columns = data.columns)

# Split the dataset into features (X) and target variable (y)
X = data.drop(columns=['isFraud'])
y = data['isFraud']

print(X)

print(y)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Assuming X_train, X_test, y_train, y_test are your training and testing datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, precision_recall_curve
import matplotlib.pyplot as plt

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))

# Plot ROC curve
fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, label='ROC curve')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Plot Precision-Recall curve
precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(X_test)[:, 1])
plt.figure(figsize=(8, 8))
plt.plot(recall, precision, label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
# Create and train the XGBoost model
model_xgb = XGBClassifier()
model_xgb.fit(X_train, y_train)

# Make predictions
y_pred_xgb = model_xgb.predict(X_test)

# Evaluate accuracy
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
print(f'XGBoost Accuracy: {accuracy_xgb:.4f}')

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Assuming y_test and y_pred_xgb are available
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
precision_xgb = precision_score(y_test, y_pred_xgb)
recall_xgb = recall_score(y_test, y_pred_xgb)
f1_xgb = f1_score(y_test, y_pred_xgb)
conf_matrix_xgb = confusion_matrix(y_test, y_pred_xgb)

print(f'XGBoost Accuracy: {accuracy_xgb:.4f}')
print(f'XGBoost Precision: {precision_xgb:.4f}')
print(f'XGBoost Recall: {recall_xgb:.4f}')
print(f'XGBoost F1-Score: {f1_xgb:.4f}')
print('XGBoost Confusion Matrix:\n', conf_matrix_xgb)

from sklearn.neighbors import KNeighborsClassifier

# Create and train the KNN model
model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)

# Make predictions
y_pred_knn = model_knn.predict(X_test)

# Evaluate accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f'KNN Accuracy: {accuracy_knn:.4f}')

# Assuming y_test and y_pred_knn are available
accuracy_knn = accuracy_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn)
recall_knn = recall_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)

print(f'KNN Accuracy: {accuracy_knn:.3f}')
print(f'KNN Precision: {precision_knn:.3f}')
print(f'KNN Recall: {recall_knn:.3f}')
print(f'KNN F1-Score: {f1_knn:.3f}')
print('KNN Confusion Matrix:\n', conf_matrix_knn)

from sklearn.linear_model import LogisticRegression

# Create and train the Logistic Regression model
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)

# Make predictions
y_pred_lr = model_lr.predict(X_test)

# Evaluate accuracy
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print(f'Logistic Regression Accuracy: {accuracy_lr:.4f}')

# Assuming y_test and y_pred_lr are available
accuracy_lr = accuracy_score(y_test, y_pred_lr)
precision_lr = precision_score(y_test, y_pred_lr)
recall_lr = recall_score(y_test, y_pred_lr)
f1_lr = f1_score(y_test, y_pred_lr)
conf_matrix_lr = confusion_matrix(y_test, y_pred_lr)

print(f'Logistic Regression Accuracy: {accuracy_lr:.4f}')
print(f'Logistic Regression Precision: {precision_lr:.4f}')
print(f'Logistic Regression Recall: {recall_lr:.4f}')
print(f'Logistic Regression F1-Score: {f1_lr:.4f}')
print('Logistic Regression Confusion Matrix:\n', conf_matrix_lr)