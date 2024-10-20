# -*- coding: utf-8 -*-
"""SpamDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SW3quI96sibl5ZgCqH8q4fX5i3i2zGVk
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load the dataset
file_path = '/content/drive/MyDrive/Colab Notebooks/datasets/spam.csv'
data = pd.read_csv(file_path, encoding='latin-1')

import matplotlib.pyplot as plt

# Calculate the percentage of spam and non-spam messages
spam_count = data['label'].value_counts()
labels = ['Not Spam', 'Spam']

# Plot a pie chart
plt.figure(figsize=(6, 6))
plt.pie(spam_count, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'orange'])
plt.title('Percentage of Spam vs Not Spam Messages')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.show()

# Clean the dataset by selecting only relevant columns
data = data[['Category', 'Message']]
data.columns = ['label', 'text']

# Convert labels to binary (0 for not spam, 1 for spam)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Create a pipeline for text preprocessing and classification
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),  # Convert text to TF-IDF features
    ('clf', MultinomialNB())  # Use Naive Bayes classifier
])

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Function to predict spam or not spam
def predict_spam(text):
    prediction = model.predict([text])
    return 'Spam' if prediction == 1 else 'Not Spam'

# Ask the user to input a message
user_input = input("Enter a message: ")
print(f"The message is: {predict_spam(user_input)}")