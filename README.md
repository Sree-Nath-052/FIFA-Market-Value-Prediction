# FIFA-Market-Value-Prediction

# Project on predicting FIFA players' market value using machine learning model

Dataset: Comprising 18,539 rows and 89 columns.

Data Visualization: Utilized Matplotlib and Seaborn.

Data Cleaning: Addressed missing values, performed string replacement, declared some as missing, and converted data types.

Encoding and Preprocessing: Applied get dummies encoding after dropping unwanted columns.

Model Training: Separated training and testing data, evaluated various models, and identified the best-performing one.

Outlier Treatment: Computed Z scores, identified outliers, and applied winsorization.

Final Model: Built a new random forest model with winsorized data achieving an R² Score of 99.26% and MAPE of 10.21%.

Deployment: Created a pickle file of the code and implemented it as a Streamlit app using PyCharm.
