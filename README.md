# Data Science and Machine Learning Portfolio

This repository contains a curated collection of LLM, NLP, retrieval, computer vision, and machine learning projects.

Each project includes a README and notebook or scaffold with the analysis workflow, modeling choices, validation results, limitations, and reproduction notes.

## Featured Research Engineering Projects

| Project | Summary | Main tools |
|---|---|---|
| [Russian LLM Pretraining and SFT](russian_llm_pretraining_and_sft) | Compact LLM training and post-training workflow covering tokenizer training, causal LM pretraining, LoRA SFT, model-card notes, and conservative evaluation reporting. | Python, PyTorch, Transformers, Tokenizers, PEFT, TRL |
| [Semantic Retrieval for arXiv Papers](arxiv_semantic_retrieval) | Dense retrieval pipeline over arXiv metadata with BGE embeddings, FAISS indexing, MRR@5 evaluation, latency profiling, and error analysis. | Python, sentence-transformers, FAISS, pandas, PyTorch |
| [Multi-Task Information Extraction on NEREL](nerel_multitask_information_extraction) | Shared-encoder PyTorch/Transformers model for token-level named entity recognition plus document-level multi-label classification. | Python, PyTorch, Transformers, Hugging Face Datasets, scikit-learn |
| [Text-to-Image Product Search with Fine-Tuned CLIP](clip_product_search) | CLIP fine-tuning and embedding-index workflow for text-to-image catalog retrieval. | Python, PyTorch, Transformers, CLIP, PIL |
| [Toxic Comment Classification](determination_of_the_tone_of_the_text) | Built a text classification pipeline to detect toxic comments for moderation. Tested BERT-based embeddings and several classifiers. | Python, pandas, BERT, NLTK, CatBoost, scikit-learn |

## Additional ML Projects

| Project | Summary | Main tools |
|---|---|---|
| [Used Car Price Prediction](determining_the_cost_of_cars) | Built a model to estimate the market value of used cars from vehicle characteristics. Compared Random Forest, CatBoost, and LightGBM models. | Python, pandas, scikit-learn, CatBoost, LightGBM |
| [Video Game Success Pattern Analysis](patterns_that_determine_the_success_of_the_game) | Analyzed global video game sales, platforms, genres, critic scores, and user scores to identify patterns associated with commercial success. | Python, pandas, NumPy, SciPy, Matplotlib |
| [Gold Recovery Process Modeling](study_of_the_technological_process_of_gold_refining) | Predicted gold recovery efficiency from mining and purification process parameters using custom sMAPE evaluation. | Python, pandas, NumPy, Matplotlib, scikit-learn |
| [Real Estate Market Analysis in Saint Petersburg](real_estate_market_analysis) | Analyzed real estate listings to estimate market value drivers and typical apartment characteristics. | Python, pandas, Matplotlib |
| [Telecom Tariff Revenue Analysis](determination_of_a_favorable_tariff_for_a_telecom_company) | Compared customer behavior and revenue between telecom tariff plans and tested statistical hypotheses. | Python, pandas, NumPy, SciPy, Matplotlib |
| [Customer Age Prediction from Images](determining_the_age_of_buyers_neural_network) | Trained a neural network to estimate customer age from facial images using a ResNet-based computer vision pipeline. | Python, TensorFlow, Keras |
| [Telecom Tariff Recommendation](tariff_recommendation) | Built a classification model that recommends one of two telecom tariffs based on monthly customer behavior. | Python, pandas, Matplotlib, scikit-learn |
| [Bank Customer Churn Prediction](forecasting_the_Bank's_customer_churn) | Predicted whether a bank customer is likely to leave, with special attention to class imbalance. | Python, pandas, Matplotlib, scikit-learn |
| [Oil Well Location Selection](choosing_a_location_for_a_well) | Used regression modeling and bootstrap simulation to select the most profitable oil extraction region under risk constraints. | Python, pandas, NumPy, scikit-learn, Bootstrap |
| [Insurance Client Data Protection](protection_of_personal_data_of_clients) | Developed and justified a linear algebra based data transformation that protects personal data without degrading model quality. | Python, pandas, NumPy, scikit-learn |
| [Taxi Order Forecasting](forecasting_taxi_orders) | Forecasted the number of taxi orders for the next hour using time-series feature engineering and regression models. | Python, pandas, scikit-learn, statsmodels, CatBoost |

## Review and Reproducibility

Each highlighted project README describes the project objective, method or architecture, data assumptions, evaluation results, limitations, and reproduction notes.

Source datasets, model checkpoints, embedding caches, private credentials, and generated large artifacts are intentionally excluded from version control.
