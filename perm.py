import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
import joblib

# Read the datasets
train = pd.read_csv(r"C:\Users\rohan\Downloads\mini\train.csv")
test = pd.read_csv(r"C:\Users\rohan\Downloads\mini\test.csv")

# Shuffle the dataset
shuftr = train.sample(frac=1).reset_index(drop=True)
shufte = test.sample(frac=1).reset_index(drop=True)

# Text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Apply text preprocessing
train["text"] = train["text"].apply(wordopt)
test["text"] = test["text"].apply(wordopt)

# Define dependent and independent variables
x_train = train["text"]
x_train_class = train["label"]
x_test = test['text']
x_test_class = test["label"]

# Vectorize the text data
vectorization = TfidfVectorizer()
vectx = vectorization.fit_transform(x_train)
vectxt = vectorization.transform(x_test)

# Initialize base classifiers
LR = LogisticRegression()
DT = DecisionTreeClassifier()
GBC = GradientBoostingClassifier(random_state=0)
RFC = RandomForestClassifier(random_state=0)

# Create a voting classifier
voting_classifier = VotingClassifier(estimators=[('lr', LR), ('dt', DT), ('gbc', GBC), ('rfc', RFC)], voting='hard')

# Check if model is already trained and saved
try:
    voting_classifier = joblib.load('voting_classifier.pkl')
    print("Model loaded successfully!")
except FileNotFoundError:
    # Train the voting classifier
    voting_classifier.fit(vectx, x_train_class)
    # Save the trained model
    joblib.dump(voting_classifier, 'voting_classifier.pkl')
    print("Model trained and saved successfully!")

#edit



# Make predictions
predictions = voting_classifier.predict(vectxt)

# Evaluate the ensemble model
print("Ensemble Model (Voting Classifier) Performance:")
print(classification_report(x_test_class, predictions))

# Function for manual testing
def manual_testing(news):
    news = wordopt(news)
    # Create a DataFrame for testing with the preprocessed news
    testing_news = pd.DataFrame({"text": [news]})
    # Vectorize the testing news
    new_x_test = vectorization.transform(testing_news["text"])
    print(news)
    # Predict using the ensemble model
    prediction = voting_classifier.predict(new_x_test)
    if prediction[0] == 0:
        print("fake")
        return "fake news"
        
    else:
        print("true")
        return "true news"
