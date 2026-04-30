# Oil Well Location Selection

## Overview

This project selects the most profitable region for oil extraction. It combines regression modeling with profit simulation and risk estimation.

## Data

Geological exploration data for three regions is stored in:

- `/datasets/geo_data_0.csv`
- `/datasets/geo_data_1.csv`
- `/datasets/geo_data_2.csv`

### Features

- `id`: unique well identifier
- `f0`, `f1`, `f2`: three meaningful but anonymized well features
- `product`: reserve volume in thousand barrels

## Objective

Use geological exploration data to choose the best oil extraction region.

## Tools and Skills

Python, pandas, NumPy, scikit-learn, linear regression, bootstrap simulation, risk analysis.

## Result

Linear Regression models were trained separately for the three regions. The second region produced the strongest risk-adjusted result: it had the highest average expected profit and the lowest estimated risk, satisfying the business risk constraint.
