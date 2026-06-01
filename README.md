# Data Science and Machine Learning Portfolio

Classic data science and machine learning projects covering tabular modeling, time-series forecasting, computer vision, statistical analysis and applied NLP.

This repository is a general portfolio archive. It focuses on supervised ML workflows, exploratory analysis, feature engineering, validation, and clear project writeups. Source datasets, model checkpoints, private credentials, generated outputs and large artifacts are intentionally excluded from version control.

## AI Research Projects Moved

The LLM, retrieval, information extraction and vision-language projects now live in [ai-research-projects](https://github.com/TrupologDS/ai-research-projects):

- Russian LLM Pretraining and SFT
- Semantic Retrieval for arXiv Papers
- Multi-Task Information Extraction on NEREL
- Text-to-Image Product Search with Fine-Tuned CLIP

## Featured Classic ML Projects

| Project | Summary | Main tools |
|---|---|---|
| [Toxic Comment Classification](determination_of_the_tone_of_the_text) | Built a text classification pipeline to detect toxic comments for moderation. Tested BERT-based embeddings and several classifiers. | Python, pandas, BERT, NLTK, CatBoost, scikit-learn |
| [Used Car Price Prediction](determining_the_cost_of_cars) | Built a model to estimate the market value of used cars from vehicle characteristics. Compared Random Forest, CatBoost, and LightGBM models. | Python, pandas, scikit-learn, CatBoost, LightGBM |
| [Customer Age Prediction from Images](determining_the_age_of_buyers_neural_network) | Trained a neural network to estimate customer age from facial images using a ResNet-based computer vision pipeline. | Python, TensorFlow, Keras |
| [Taxi Order Forecasting](forecasting_taxi_orders) | Forecasted the number of taxi orders for the next hour using time-series feature engineering and regression models. | Python, pandas, scikit-learn, statsmodels, CatBoost |

## Additional ML Projects

| Project | Summary | Main tools |
|---|---|---|
| [Video Game Success Pattern Analysis](patterns_that_determine_the_success_of_the_game) | Analyzed global video game sales, platforms, genres, critic scores, and user scores to identify patterns associated with commercial success. | Python, pandas, NumPy, SciPy, Matplotlib |
| [Gold Recovery Process Modeling](study_of_the_technological_process_of_gold_refining) | Predicted gold recovery efficiency from mining and purification process parameters using custom sMAPE evaluation. | Python, pandas, NumPy, Matplotlib, scikit-learn |
| [Real Estate Market Analysis in Saint Petersburg](real_estate_market_analysis) | Analyzed real estate listings to estimate market value drivers and typical apartment characteristics. | Python, pandas, Matplotlib |
| [Telecom Tariff Revenue Analysis](determination_of_a_favorable_tariff_for_a_telecom_company) | Compared customer behavior and revenue between telecom tariff plans and tested statistical hypotheses. | Python, pandas, NumPy, SciPy, Matplotlib |
| [Telecom Tariff Recommendation](tariff_recommendation) | Built a classification model that recommends one of two telecom tariffs based on monthly customer behavior. | Python, pandas, Matplotlib, scikit-learn |
| [Bank Customer Churn Prediction](forecasting_the_Bank's_customer_churn) | Predicted whether a bank customer is likely to leave, with special attention to class imbalance. | Python, pandas, Matplotlib, scikit-learn |
| [Oil Well Location Selection](choosing_a_location_for_a_well) | Used regression modeling and bootstrap simulation to select the most profitable oil extraction region under risk constraints. | Python, pandas, NumPy, scikit-learn, Bootstrap |
| [Insurance Client Data Protection](protection_of_personal_data_of_clients) | Developed and justified a linear algebra based data transformation that protects personal data without degrading model quality. | Python, pandas, NumPy, scikit-learn |

## Review and Reproducibility

Each project folder contains a README and notebook with the analysis workflow, modeling choices, validation results, limitations and reproduction notes.

Metrics are project-local results from the documented notebooks and should not be treated as broad benchmarks. Source datasets, model checkpoints, embedding caches, private credentials and generated artifacts are not committed.
