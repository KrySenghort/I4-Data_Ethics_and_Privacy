import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

# Load dataset
df = pd.read_csv('dataset_formal.csv')
df = df.drop(df.columns[0], axis=1)
df = df.drop_duplicates()
df = df.dropna()

# Encode labels using mapping
encoding_map = {
    'true':5,
    'mostly-true':4,
    'half-true':3,
    'barely-true':2,
    'false':1,
    'pants-fire':0
}
data = {'label': ['pants-fire','false','barely-true','half-true','mostly-true','true']}
df['label'] = df['label'].map(encoding_map)

# NLP processing
df['text'] = df['title'] + '. ' + df['text']

# Remove 
import string
def remove_special_chars(text):
    # Remove special characters using string.punctuation
    return ''.join(char for char in text if char not in string.punctuation)

df['text'] = df['text'].apply(remove_special_chars)

# stopword analytics
from nltk.corpus import stopwords          # check the stopword and remove out.
from nltk.stem.porter import PorterStemmer # stemmer remove suffix and prefix and return the root word.
import nltk 

# Tokenization and stemming
port_sem = PorterStemmer()
def stemming(statement):
    stemmed_content = re.sub('[^a-zA-Z]',' ',statement)  # searching paragraph or text
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_sem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
df['text'] = df['text'].apply(stemming)

# separating data and label
X = df['text']
Y = df['label']
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.25,random_state=0)

# TF-IDF Vectorization
vector = TfidfVectorizer()
tf_fit = vector.fit(X_train)
X_train_tf = tf_fit.transform(X_train)
X_test_tf = tf_fit.transform(X_test)

# Model training
def train_models(X_train, y_train):
    ds = DecisionTreeClassifier(criterion='entropy', random_state=0)
    ds.fit(X_train, y_train)
    return ds

# Perform model training
md = train_models(X_train_tf, y_train)

# Streamlit app
def main():
    
    st.image('logo.png')
    st.title("Fake News Detection App")

    # User input
    user_input1 = st.text_input("Enter news's title ")
    user_input2 = st.text_input("Enter news's text:")
    
    # Tokenize and stem user input
    user_input = user_input1 + '. ' + user_input2
    input_text = stemming(user_input)

    # Vectorize user input
    vectorized_input = vector.transform([input_text])

    # Make predictions
    pred = md.predict(vectorized_input)
    st.write("Prediction Results:")
       
    if pred==0:
        st.write('The news is pant on fire')

    elif pred==1:
        st.write('The news is false')

    elif pred==2:
        st.write("the news is barely true")

    elif pred==3:        
        st.write('The news is half-true')

    elif pred==4:
        st.write('The news is mostly true')

    elif pred==5:
        st.write('The news is true')

    else:
        st.write('The news is unknown')


