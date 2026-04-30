# Gold Recovery Process Modeling

## Overview

This project develops a machine learning model for an industrial gold recovery process. The model predicts the recovery coefficient of gold from ore using process parameters from extraction and purification stages.

## Data

The project uses three datasets:

- `gold_recovery_train_new.csv`: training set
- `gold_recovery_test_new.csv`: test set
- `gold_recovery_full_new.csv`: full source data

## Process Description

- `Rougher feed`: raw material
- `Rougher additions` / `reagent additions`: flotation reagents such as xanthate, sulphate, and depressant
- `Xanthate`: flotation promoter or activator
- `Sulphate`: sodium sulphide in this production process
- `Depressant`: sodium silicate
- `Rougher process`: flotation stage
- `Rougher tails`: tailings
- `Float banks`: flotation unit
- `Cleaner process`: purification stage
- `Rougher Au`: rougher gold concentrate
- `Final Au`: final gold concentrate

## Stage Parameters

- `air amount`: air volume
- `fluid levels`: fluid level
- `feed size`: raw material particle size
- `feed rate`: feed rate

## Objective

Predict gold concentration and recovery efficiency during the purification process.

## Tools and Skills

Python, pandas, NumPy, Matplotlib, scikit-learn, exploratory data analysis, custom sMAPE metric, regression modeling.

## Result

The project combined multiple datasets, explored process-stage patterns, and implemented the sMAPE metric for evaluation. Gold concentration increased across processing stages, while silver and lead behaved differently. A Random Forest model produced the best final performance.
