# Insurance Client Data Protection

## Overview

This project designs a data transformation method for an insurance company that needs to protect client personal data. The transformation should make personal information difficult to recover while preserving model quality.

## Data

The `insurance` table contains client information.

### Features

- `gender`: gender
- `age`: age
- `salary`: salary
- `family_members`: number of family members

### Target

- `insurance_payouts`: number of insurance payouts received by the client over the last five years

## Objective

Develop and justify a personal data anonymization method.

## Tools and Skills

Python, pandas, NumPy, scikit-learn, linear algebra, data transformation, regression evaluation.

## Result

The project proposed, justified, and implemented an encryption-like transformation based on multiplying features by an invertible matrix. The model quality remained unchanged after transformation, confirming that the method preserves predictive performance.
