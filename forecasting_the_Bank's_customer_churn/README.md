# Bank Customer Churn Prediction

## Overview

This project predicts whether a bank customer is likely to leave. Retaining existing customers is cheaper than acquiring new ones, so the model supports proactive retention efforts.

## Data

The `Churn` table contains customer information.

### Features

- `RowNumber`: row index
- `CustomerId`: unique customer identifier
- `Surname`: surname
- `CreditScore`: credit score
- `Geography`: country of residence
- `Gender`: gender
- `Age`: age
- `Tenure`: number of years as a bank customer
- `Balance`: account balance
- `NumOfProducts`: number of bank products used
- `HasCrCard`: whether the customer has a credit card
- `IsActiveMember`: whether the customer is active
- `EstimatedSalary`: estimated salary

### Target

- `Exited`: whether the customer left the bank

## Objective

Predict customers who may leave the bank in the near future.

## Tools and Skills

Python, pandas, Matplotlib, scikit-learn, class imbalance handling, classification modeling.

## Result

The workflow included missing-value handling, feature removal, encoding, and class imbalance treatment with upsampling and downsampling. RandomForestClassifier performance improved substantially after addressing class imbalance.
