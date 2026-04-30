# Used Car Price Prediction

## Overview

This project builds a machine learning model for a used-car sales service. The goal is to estimate a vehicle's market value from its technical and listing characteristics so that customers can quickly understand a fair selling price.

## Data

The dataset contains vehicle listing information from the `autos` table.

### Features

- `DateCrawled`: date when the listing was downloaded from the database
- `VehicleType`: vehicle body type
- `RegistrationYear`: vehicle registration year
- `Gearbox`: gearbox type
- `Power`: engine power in horsepower
- `Model`: vehicle model
- `Kilometer`: mileage in kilometers
- `RegistrationMonth`: vehicle registration month
- `FuelType`: fuel type
- `Brand`: vehicle brand
- `Repaired`: whether the vehicle has been repaired
- `DateCreated`: listing creation date
- `NumberOfPictures`: number of vehicle photos
- `PostalCode`: owner's postal code
- `LastSeen`: date of the user's last activity

### Target

- `Price`: vehicle price in euros

## Objective

Develop a recommendation system that predicts a car's value from its description.

## Tools and Skills

Python, pandas, scikit-learn, CatBoost, LightGBM, data preprocessing, cross-validation, regression modeling.

## Result

The project included extensive data preprocessing, model comparison, and cross-validation. RandomForestRegressor, CatBoostRegressor, and LightGBM were evaluated, and LightGBM produced the best results.
