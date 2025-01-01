# IMDB Sentiment Analysis Web App

This is a simple web application for analyzing the sentiment (Positive/Negative) of movie reviews using a trained machine learning model. The app is built using **Streamlit** and a pre-trained sentiment analysis model based on the IMDB dataset.

## Features
- Input a movie review to analyze its sentiment.
- Displays the predicted sentiment (Positive or Negative) along with the confidence score.
- Handles invalid inputs gracefully.

## How It Works
1. A pre-trained Keras model is used to classify reviews as positive or negative.
2. User input is preprocessed (encoded and padded) to match the model's requirements.
3. The app outputs the predicted sentiment and confidence score.

## Installation
To run this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed-J646/NLP-Sentiment-Analysis-IMDB.git
   cd imdb-sentiment-analysis

Install the required Python packages:


pip install -r requirements.txt
Ensure the pre-trained model file (imdb_sentiment_model.h5) is in the same directory as the app script.

Run the app:


streamlit run app.py

Project Files

app.py: The main script for the Streamlit web app.

imdb_sentiment_model.h5: Pre-trained Keras model for sentiment analysis.
requirements.txt: List of Python packages required to run the app.
README.md: Documentation for the project.
Requirements
Python 3.7+
Streamlit
TensorFlow
NumPy

Example Usage
Run the app using streamlit run app.py.
Enter a movie review in the input box.
Click the "Analyze Sentiment" button to see the predicted sentiment and confidence score.
Pre-trained Model
The model is trained on the IMDB dataset for binary sentiment classification (Positive/Negative). It uses:

An embedding layer to process text data.
LSTM for capturing sequential patterns in text.
Fully connected layers for classification.
Screenshot

License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

Acknowledgements
Dataset: IMDB Dataset of 50K Movie Reviews
Framework: Streamlit
Library: TensorFlow
