import streamlit as st
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pickle

# Ensure required NLTK data is downloaded
nltk.download('names')

# Define features (words) and their corresponding labels (emotions)
def word_features(words):
    return dict([(word, True) for word in words])

# Define sets of words for each emotion
happy_words = ['happy', 'joyful', 'pleased', 'thrilled', 'ecstatic']
sad_words = ['sad', 'unhappy', 'depressed', 'gloomy', 'miserable']
angry_words = ['angry', 'furious', 'irritated', 'mad', 'enraged']
excited_words = ['excited', 'enthusiastic', 'thrilled', 'eager', 'animated']
nervous_words = ['nervous', 'anxious', 'worried', 'apprehensive', 'tense']
scared_words = ['scared', 'fearful', 'terrified', 'panicked', 'anxious']

# Create feature sets for each emotion
happy_features = [(word_features([hap_word]), 'happy') for hap_word in happy_words]
sad_features = [(word_features([sad_word]), 'sad') for sad_word in sad_words]
angry_features = [(word_features([ang_word]), 'angry') for ang_word in angry_words]
excited_features = [(word_features([exc_word]), 'excited') for exc_word in excited_words]
nervous_features = [(word_features([ner_word]), 'nervous') for ner_word in nervous_words]
scared_features = [(word_features([sca_word]), 'scared') for sca_word in scared_words]

# Combine feature sets for all emotions
train_set = happy_features + sad_features + angry_features + excited_features + nervous_features + scared_features

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Save the trained classifier
filename = 'emotion_classifier_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# Streamlit Application
st.title("Emotion Analyzer")
message = st.text_input("Tell me what you feel today: ")

# Load the trained Naive Bayes classifier from the saved file
loaded_model = pickle.load(open(filename, 'rb'))

message_tone = loaded_model.classify(word_features(message.split()))

# Define the function for the button click
def sayFeeling():
    st.write(f"The emotion you are feeling is: {message_tone}")

# Button to classify the entered message
st.button('Analyze Emotion', on_click=sayFeeling)

# To run the app, use the command in terminal:
# python -m streamlit run your_script_name.py
