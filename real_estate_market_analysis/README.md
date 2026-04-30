# Real Estate Market Analysis in Saint Petersburg

## Overview

This project analyzes residential real estate listings from Yandex Real Estate. The goal is to estimate market value drivers and identify typical apartment characteristics in and around Saint Petersburg.

## Data

The `real_estate_data` table contains property listing characteristics.

### Features

- `airports_nearest`: distance to the nearest airport in meters
- `balcony`: number of balconies
- `ceiling_height`: ceiling height in meters
- `cityCenters_nearest`: distance to the city center in meters
- `days_exposition`: number of days the listing was published
- `first_day_exposition`: publication date
- `floor`: apartment floor
- `floors_total`: total number of floors in the building
- `is_apartment`: whether the listing is an apartment
- `kitchen_area`: kitchen area in square meters
- `last_price`: final listing price
- `living_area`: living area in square meters
- `locality_name`: locality name
- `open_plan`: whether the apartment has an open plan
- `parks_around3000`: number of parks within a 3 km radius
- `parks_nearest`: distance to the nearest park in meters
- `ponds_around3000`: number of ponds within a 3 km radius
- `ponds_nearest`: distance to the nearest pond in meters
- `rooms`: number of rooms
- `studio`: whether the apartment is a studio
- `total_area`: total area in square meters
- `total_images`: number of listing photos

## Objective

Use real estate listing data to estimate property market values and describe typical apartment parameters.

## Tools and Skills

Python, pandas, Matplotlib, exploratory data analysis, data visualization, data preprocessing.

## Result

The project included duplicate removal, anomaly handling, missing-value imputation, type conversion, and text normalization. The analysis found that many listings came from five- and nine-story buildings, and the city center boundary was estimated at roughly 3 km based on a sharp change in price behavior.
