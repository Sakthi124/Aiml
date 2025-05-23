PROGRAM:

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

# Load dataset

data = pd.read_excel('your_dataset.xlsx')

# Features and target

X = data[['GPA', 'SAT_Score', 'Extracurriculars']]

y = data['Admission']

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model

model = LogisticRegression()

model.fit(X_train, y_train)

# Plot GPA vs SAT with color by admission

plt.figure(figsize=(8, 6))

scatter = plt.scatter(data['GPA'], data['SAT_Score'], c=data['Admission'], 

cmap='coolwarm', edgecolor='k')

plt.xlabel('GPA')

plt.ylabel('SAT Score')

plt.title('Student Admission (GPA vs SAT)')

plt.colorbar(scatter, label='Admission (0 = No, 1 = Yes)')

plt.grid(True)

plt.show(
