# Telecom Tariff Revenue Analysis

## Overview

This project analyzes customer behavior for two telecom tariff plans. The goal is to compare usage patterns, estimate revenue, and test whether revenue differs by tariff and by customer location.

## Data

The project uses several telecom datasets.

### `users`: user information

- `user_id`: unique user identifier
- `first_name`: user's first name
- `last_name`: user's last name
- `age`: user's age in years
- `reg_date`: tariff activation date
- `churn_date`: tariff cancellation date; missing values indicate that the tariff was active when the data was extracted
- `city`: user's city
- `tarif`: tariff plan name

### `calls`: call information

- `id`: unique call identifier
- `call_date`: call date
- `duration`: call duration in minutes
- `user_id`: identifier of the user who made the call

### `messages`: message information

- `id`: unique message identifier
- `message_date`: message date
- `user_id`: identifier of the user who sent the message

### `internet`: internet session information

- `id`: unique session identifier
- `mb_used`: traffic used during the session in megabytes
- `session_date`: internet session date
- `user_id`: user identifier

### `tariffs`: tariff information

- `tariff_name`: tariff name
- `rub_monthly_fee`: monthly fee in rubles
- `minutes_included`: monthly included minutes
- `messages_included`: monthly included messages
- `mb_per_month_included`: monthly included traffic in megabytes
- `rub_per_minute`: price per extra minute
- `rub_per_message`: price per extra message
- `rub_per_gb`: price per extra gigabyte

## Objective

Analyze customer behavior and determine which tariff is more profitable for the telecom operator.

## Tools and Skills

Python, pandas, NumPy, SciPy, Matplotlib, exploratory data analysis, hypothesis testing.

## Result

The data was aggregated into monthly user-level records containing tariff, calls, messages, traffic, and revenue. Usage distributions were compared between tariffs, and statistical hypotheses were tested. There was enough evidence to conclude that revenue differs between Ultra and Smart users, while the analysis did not find sufficient evidence that Moscow and non-Moscow user revenue differs.
