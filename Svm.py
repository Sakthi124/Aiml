import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.svm import SVC

from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset from an Excel file

df = pd.read_excel('data.xlsx') # Replace 'data.xlsx' with your actual file path

# Step 2: Preprocess the data

# Assuming the dataset has 'Feature1', 'Feature2' for features and 'Class' for target

X = df[['Feature1', 'Feature2']] # Replace with your actual feature columns
y = df['Class'] # Replace with your actual target column

# Step 3: Encode the target variable (Class) into numeric values

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

# Step 4: Train an SVM model

model = SVC(kernel='linear')

model.fit(X, y_encoded)

# Step 5: Calculate margin (2 / ||w||)

w = model.coef_[0] # Extract weight vector (coefficients)

margin = 2 / np.linalg.norm(w) # Margin = 2 / ||w||

print(f"Maximum margin: {margin:.4f}")

# Step 6: Plot the decision boundary (if 2D features)

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_encoded, cmap='coolwarm', marker='o') # Data 

points

# Plot decision boundary

b = model.intercept_[0]

x_vals = np.linspace(X.iloc[:, 0].min(), X.iloc[:, 0].max(), 100)

y_vals = -(w[0] * x_vals + b) / w[1]

plt.plot(x_vals, y_vals, 'k--', label='Decision Boundary')

# Highlight the support vectors

support_vectors = model.support_vectors_ # The actual support vectors

plt.scatter(support_vectors[:, 0], support_vectors[:, 1], facecolors='none', 

edgecolors='red', s=100, label="Support Vectors")

plt.xlabel('Feature 1')

plt.ylabel('Feature 2')

plt.title('SVM Decision Boundary with Support Vectors')

plt.legend()

plt.grid(True)

plt.show()
