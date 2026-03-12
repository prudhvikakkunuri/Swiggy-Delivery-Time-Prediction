Swiggy Delivery Time Prediction
This repository contains a machine learning solution designed to predict the Estimated Time of Arrival (ETA) for Swiggy food deliveries. By leveraging historical logistics, environmental data, and rider details, this project provides a scalable tool to improve customer trust and operational efficiency.

📌 Project Overview
In the food delivery industry, ETA accuracy is a critical factor for customer satisfaction. Inaccurate predictions lead to reduced trust, increased cancellations, and inefficient rider management. This project follows the CRISP-ML(Q) methodology to build a production-ready system.

Key Objectives:

Predict per-order delivery time in minutes at the moment an order is placed.


Dynamic updates to ensure business-grade accuracy.


Operational Optimization to reduce idle and overtime costs for delivery partners.

📊 Dataset Overview
The project analyzed a comprehensive dataset consisting of approximately 50,000 records.

Category	Key Features
Rider Details	
Age, Ratings, Vehicle Type, and Condition

Logistics	
Distance (km), Multiple Deliveries, and City Type

Order Details	
Type of Order (snack, meal, etc.) and Prep Time

Environmental	
Weather (sunny, stormy, etc.) and Traffic (low to jam)

Temporal	
Hour of Day, Day of Week, Weekend, and Festival status

Target Variable	

Time Taken (Actual delivery time in minutes)


Export to Sheets

🛠️ Data Strategy & Engineering
Data Preprocessing

Imputation: Missing values were handled using rider-wise means for age/ratings and mode/median for categorical and numerical features.


Outlier Removal: Identified and removed "impossible" data points, such as delivery speeds exceeding 100 km/h, to ensure data quality.

Encoding:


One-Hot Encoding: Applied to weather, city, and type_of_order.


Ordinal Encoding: Applied to traffic levels (Low < Medium < High < Jam).


Scaling: Used StandardScaler to bring numerical features like distance and age to the same scale.

Feature Selection
To reduce noise and dimensionality, I moved from 26 raw features to a refined set using multiple techniques:


Correlation Analysis: Checked relationships between features and the target variable.


Mutual Information: Identified the most predictive variables based on information gain.


Final Selected Features: Included distance, traffic, age, ratings, multiple deliveries, and temporal features.

🤖 Modeling & Evaluation
I experimented with a hierarchy of models to find the most robust solution:


Linear Regression 


Ridge & Lasso Regression 


K-Nearest Neighbors (KNN) 


Random Forest Regressor (Final Choice) 

Optimization

Cross-Validation: Used 5-Fold Cross Validation to ensure stable performance across different data splits.


Hyperparameter Tuning: Utilized GridSearchCV and RandomizedSearchCV to optimize parameters like n_estimators and max_depth.

🚀 Deployment
The final model was deployed as a real-time web application:


Framework: Streamlit.


Integration: Saved the model using pickle for quick loading.


Functionality: Users can input rider details, distance, and traffic conditions to receive an instant ETA in minutes.

👨‍💻 Author

Kakunuri Prudhvi 


Education: Computer Science Engineering Graduate, ASTI 


Portfolio: prudhvikakkunuri.github.io 


LinkedIn: linkedin.com/in/prudhvi-k-387257222 


GitHub: github.com/prudhvikakkunuri 


This project was completed as part of the curriculum at Innomatics Research Labs.
