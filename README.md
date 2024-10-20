**Spam Classification Project**
**This project uses Natural Language Processing (NLP) and machine learning to classify SMS messages as either "spam" or "not spam."**

**Features**
**Input**: SMS messages.
**Output**: Classification of messages as "Spam" or "Not Spam."

**Steps to Run the Project
Install Dependencies:**

Python 3.x
**Required libraries:**
**Copy code**
pip install pandas scikit-learn matplotlib
**Dataset:** The dataset used is spam.csv, which contains SMS messages with labels "ham" (not spam) and "spam."

**Execution:**

Run the Python script to load the dataset, train the model, and test its performance.
**Model Training:**

The model is trained using the Naive Bayes classifier and TF-IDF vectorizer for text processing.
**Visualization:**

A pie chart shows the percentage of spam and non-spam messages.
**Example**
**Input**: "Congratulations! You've won a $1000 gift card."
**Output**: Spam
How to Use
After training the model, input a custom message and the model will predict whether it's "Spam" or "Not Spam."
