import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.datasets import imdb

# Load the trained model
model = load_model("imdb_sentiment_model.h5")

# Load IMDB word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Functions
def encode_review(review, word_index, maxlen=200):
    encoded = [word_index.get(word, 2) for word in review.split()]
    return pad_sequences([encoded], maxlen=maxlen, padding='post', truncating='post')

def decode_review(encoded_review):
    return " ".join([reverse_word_index.get(i - 3, "?") for i in encoded_review])

# Streamlit UI
st.title("IMDB Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment!")

# Input text
review = st.text_area("Enter Review:", placeholder="Type your review here...")

if st.button("Analyze Sentiment"):
    if review.strip():
        encoded_review = encode_review(review.lower(), word_index)
        prediction = model.predict(encoded_review)[0][0]
        sentiment = "Positive" if prediction > 0.5 else "Negative"
        st.write(f"**Predicted Sentiment:** {sentiment}")
        st.write(f"**Confidence Score:** {prediction:.2f}")
    else:
        st.warning("Please enter a valid review.")
