import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier, plot_tree

import matplotlib.pyplot as plt

# Step 1: Define dataset

data = {

 'Age': ['Youth', 'Youth', 'Middle-aged', 'Senior', 'Senior', 'Senior',

 'Middle-aged', 'Youth', 'Youth', 'Senior', 'Youth', 'Middle-aged',

 'Middle-aged', 'Senior'],

 'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low',

 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium',

 'High', 'Medium'],

 'Student': ['No', 'No', 'No', 'No', 'Yes', 'Yes',

 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No',

 'Yes', 'No'],

 'Credit_rating': ['Fair', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent',

 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent',

 'Fair', 'Excellent'],

 'Buys_computer': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No',

 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes',

 'Yes', 'No']

}

df = pd.DataFrame(data)

# Step 2: Encode data

le = LabelEncoder()

for column in df.columns:

 df[column] = le.fit_transform(df[column])
# Step 3: Define features and target

X = df.drop('Buys_computer', axis=1)

y = df['Buys_computer']

# Step 4: Train the model

model = DecisionTreeClassifier(criterion='entropy')

model.fit(X, y)

# Step 5: Plot the tree

plt.figure(figsize=(10, 6))

plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)

plt.title("Decision Tree - Buys Computer")

plt.show()

OUTPUT:
