import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split

import numpy as np

import pandas as pd

# Step 1: Load the dataset (assuming you have preprocessed features in an Excel file)
# Example: Features and labels are in the dataset (cat = 1, dog = 0)

dataset = pd.read_excel("dataset_features.xlsx") # Update the path

# Step 2: Separate the features (input) and labels (output)

# Assuming last column is the label (1 for cat, 0 for dog) and all other columns are 

features

features = dataset.iloc[:, :-1].values # All columns except last (features)

labels = dataset.iloc[:, -1].values # The last column (labels)

# Step 3: Split the dataset into training and test sets (80% train, 20% test)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, 

random_state=42)

# Step 4: Build a simple neural network model

model = Sequential([

 Dense(128, input_dim=X_train.shape[1], activation='relu'), # First hidden layer (128 

neurons)

 Dense(64, activation='relu'), # Second hidden layer (64 neurons)

 Dense(1, activation='sigmoid') # Output layer with sigmoid activation (binary 

classification)

])

# Step 5: Compile the model

model.compile(optimizer=Adam(learning_rate=0.0001), 

 loss='binary_crossentropy', 

 metrics=['accuracy'])

# Step 6: Train the model

history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, 

y_test))

# Step 7: Evaluate the model on the test data

loss, accuracy = model.evaluate(X_test, y_test)

print(f"Test Accuracy: {accuracy * 100:.2f}%")
# Step 8: Get the model's weights after training

# The weights of the model can be accessed via the `model.get_weights()` method.

weights = model.get_weights()

# The weights are a list of NumPy arrays: 

# 1. The weights for the first layer (input to hidden)

# 2. The weights for the second layer (hidden to hidden)

# 3. The weights for the output layer (hidden to output)

print("Weights of the model after training:")

# For each layer, display the shape of the weights

for i, weight_matrix in enumerate(weights):

 print(f"Layer {i+1} weights shape: {weight_matrix.shape}")

# Optional: Accessing individual weight matrices

# Example: Weights of the first layer

first_layer_weights = weights[0]

print(f"First layer weights:\n{first_layer_weights}")

# Optional: Plotting the training history

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Training Accuracy')

plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.xlabel('Epochs')

plt.ylabel('Accuracy')

plt.legend()

plt.title('Training and Validation Accuracy')

plt.show()

OUTPUT:

Epoch 1/10

1/1 ━━━━━━━━━━━━━━━━━━━━ 2s 2s/step - accuracy: 0.7500 - loss: 

0.6866 - val_accuracy: 1.0000 - val_loss: 0.675
