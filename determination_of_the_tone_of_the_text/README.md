# Toxic Comment Classification

## Overview

This project builds a text classification model for an online store that allows users to edit product descriptions and comment on other users' changes. The business needs an automated moderation tool that can identify toxic comments.

## Data

The `toxic_comments` table contains:

- `text`: comment text
- `toxic`: target label indicating whether the comment is toxic

## Objective

Train a model that classifies user comments as toxic or non-toxic.

## Tools and Skills

Python, pandas, BERT, NLTK, TF-IDF, CatBoost, scikit-learn, text preprocessing, classification modeling.

## Result

The workflow included tokenization, padding, attention masks, BERT embeddings, and comparison of LogisticRegression, RandomForestClassifier, and CatBoostClassifier. CatBoostClassifier achieved the strongest result in the experiment.
