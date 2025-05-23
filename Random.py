import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

# Load the dataset from Excel

df = pd.read_excel('fruit_data.xlsx')

# Convert 'Fruit Type' to numerical values
df['Fruit_Type_Label'] = df['Fruit Type'].map({'Apple': 0, 'Orange': 1, 'Banana': 2})

# Define the features (X) and target variable (y)

X = df[['Weight (g)', 'Color (encoded)', 'Size (cm)', 'Shape (encoded)']] # Features

y = df['Fruit_Type_Label'] # Target

# Split the data into training and testing sets (70% training, 30% testing)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Random Forest classifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

# Predict the test set results

y_pred = rf_model.predict(X_test)

# Evaluate the accuracy of the model

accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')

# Example of predicting a new fruit

def predict_fruit(weight, color, size, shape):

 prediction = rf_model.predict([[weight, color, size, shape]])

 fruit_types = {0: 'Apple', 1: 'Orange', 2: 'Banana'}

 print(f'The predicted fruit is: {fruit_types[prediction[0]]}')

predict_fruit(160, 1, 6, 1) 
