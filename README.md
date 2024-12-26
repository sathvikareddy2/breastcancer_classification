# Breast Cancer Classification

## Overview
Breast cancer is one of the most common forms of cancer worldwide, and early detection is essential for improving the survival rate of affected individuals. The ability to identify whether a tumor is benign or malignant through diagnostic measures can greatly assist medical professionals in making informed decisions for treatment. This project is an automated machine learning-based system designed to predict whether a breast cancer tumor is malignant or benign based on diagnostic features. The system uses a dataset containing various measurements related to tumor cells and applies machine learning algorithms to classify these tumors.

## Primary Goal
This project focuses on building a machine learning-based system to classify breast cancer tumors as malignant or benign. Using a dataset with features derived from breast mass measurements, four machine learning models were implemented:  
- Logistic Regression (achieved the best accuracy)  
- Support Vector Machine (SVM) (achieved the best accuracy)  
- Random Forest  
- Decision Tree  

The top-performing models, Logistic Regression and SVM, Logistic Regression was deployed using Flask.

---

## Dataset Details
The dataset contains 30 features derived from breast mass measurements. These features include:  
- **Features**: Radius, Perimeter, Area, Smoothness, Compactness, Concavity, Concave Points, Symmetry, Fractal Dimension.  
- **Types of Measurement**:  
  - Mean values  
  - Standard Error (SE)  
  - Worst values  
- **Initial Features**: 30 (10 features × 3 types).  
- **Final Features**: 22 (after removing highly correlated features to reduce multicollinearity).

---

## Models Implemented
1. **Logistic Regression**:  
   - Achieved one of the best accuracies.
   - Used for deployment via Flask.
   - Model saved using Python's `pickle` module.

2. **Support Vector Machine (SVM)**:  
   - Achieved accuracy comparable to Logistic Regression.
   - Effective in handling high-dimensional data.

3. **Random Forest**:  
   - Provided good accuracy and insights into feature importance.
   - Useful for feature selection.

4. **Decision Tree**:  
   - Offered interpretability but lower accuracy compared to Logistic Regression and SVM.

---

## Technology Stack
- **Programming Language**: Python  
- **Web Framework**: Flask(for the user interface)
- **Model Persistence**: Pickle (for saving and loading Logistic Regression model)  

---

## Implementation Steps
1. **Data Preprocessing**:  
   - Removed highly correlated features, reducing the feature set from 30 to 22.  
   - Normalized features for improved model performance.

2. **Model Training**:  
   - Trained Logistic Regression, SVM, Random Forest, and Decision Tree models.  
   - Evaluated models using accuracy, precision, and recall metrics.

3. **Deployment**:  
   - Logistic Regression model saved using `pickle`.  
   - Flask-based web interface for user interaction and prediction.

---

## Features

- **radius_mean**: The average radius of the tumor cell.  
- **radius_se**: The standard error of the tumor cell's radius.  
- **radius_worst**: The largest radius of the tumor cell.  
- **perimeter_mean**: The average perimeter of the tumor cell.  
- **perimeter_se**: The standard error of the tumor cell's perimeter.  
- **perimeter_worst**: The largest perimeter of the tumor cell.  
- **area_mean**: The average area of the tumor cell.  
- **area_se**: The standard error of the tumor cell's area.  
- **area_worst**: The largest area of the tumor cell.  
- **smoothness_mean**: The average smoothness of the tumor's surface.  
- **smoothness_se**: The standard error of the tumor's smoothness.  
- **smoothness_worst**: The worst smoothness score of the tumor's surface.  
- **compactness_mean**: The average compactness of the tumor (a measure of shape irregularity).  
- **compactness_se**: The standard error of the tumor's compactness.  
- **compactness_worst**: The worst compactness score of the tumor.  
- **concavity_mean**: The average concavity of the tumor (the presence of indentations).  
- **concavity_se**: The standard error of the tumor's concavity.  
- **concavity_worst**: The worst concavity score of the tumor.  
- **concave_points_mean**: The average number of concave points (indentations) on the tumor’s surface.  
- **concave_points_se**: The standard error of the tumor's concave points.  
- **concave_points_worst**: The worst concave points score of the tumor.  
- **symmetry_mean**: The average symmetry of the tumor’s shape.  
- **symmetry_se**: The standard error of the tumor's symmetry.  
- **symmetry_worst**: The worst symmetry score of the tumor.  
- **fractal_dimension_mean**: The average fractal dimension of the tumor, which measures the complexity of the tumor's surface.  
- **fractal_dimension_se**: The standard error of the tumor's fractal dimension.  
- **fractal_dimension_worst**: The worst fractal dimension score of the tumor.  

---

## How to Run

### Prerequisites
- Python 3.7 or later installed on your system.
- Clone the repository using Git.

### Steps to Run the Project
1. Clone the repository:
   bash
   git clone https://github.com/sathvikareddy2/breastcancer_classification.git
   cd your-repo
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the Flask application:
   python app.py
5. Open your web browser and navigate to:
   http://127.0.0.1:5000
