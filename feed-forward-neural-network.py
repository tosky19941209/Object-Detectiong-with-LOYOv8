import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
print('Tensorflow version:', tf.__version__)

# Create a toy dataset
# Input data
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# # Output data
# y = np.array([0, 1, 1, 0])
#
# # Create a neural network model
# model = Sequential()
# model.add(Dense(4, input_dim=2, activation='relu'))  # Input layer with 2 inputs and 4 neurons
# model.add(Dense(1, activation='sigmoid'))  # Output layer with 1 neuron and sigmoid activation function
#
# # Compile the model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# # Train the model
# model.fit(X, y, epochs=1000, verbose=0)
#
# # Make predictions
# predictions = model.predict(X)
# print(predictions)