# Taxi Order Forecasting

## Overview

This project forecasts taxi demand for the next hour using historical airport taxi order data. The forecast helps the company attract more drivers during peak demand periods.

## Data

The `taxi` table contains:

- `num_orders`: number of taxi orders at a given timestamp

## Objective

Build a model that predicts hourly taxi order volume.

## Tools and Skills

Python, pandas, scikit-learn, statsmodels, CatBoost, time-series analysis, feature engineering, regression modeling.

## Result

The project analyzed trend and seasonality, showing that the minimum number of orders occurred around 6 a.m. and the maximum around midnight. Time-based features were added, and LinearRegression, RandomForestRegressor, and CatBoostRegressor were compared. Linear Regression produced the best result.
