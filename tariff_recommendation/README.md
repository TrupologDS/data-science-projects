# Telecom Tariff Recommendation

## Overview

This project builds a classification model for a mobile operator whose customers are still using legacy tariffs. The model recommends one of the newer tariff plans based on monthly user behavior.

## Data

The `users_behavior` table contains monthly customer behavior.

### Features

- `calls`: number of calls
- `minutes`: total call duration in minutes
- `messages`: number of SMS messages
- `mb_used`: internet traffic used in megabytes

### Target

- `is_ultra`: tariff used during the month; Ultra is 1 and Smart is 0

## Objective

Recommend the most suitable tariff for a customer based on their usage behavior.

## Tools and Skills

Python, pandas, Matplotlib, scikit-learn, classification modeling, model evaluation.

## Result

The project prepared the data and compared Decision Tree, Logistic Regression, and Random Forest models. The Random Forest model performed best, reaching an accuracy of 0.81.
