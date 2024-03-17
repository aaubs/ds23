import requests
import streamlit as st

def fetch_jokes():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single&amount=5'
    response = requests.get(url)
    data = response.json()
    return data['jokes']

def display_jokes(jokes):
    for joke in jokes:
        with st.container():
            st.markdown(f"**Category**: {joke['category']} | **Safe**: {'Yes' if joke['safe'] else 'No'}", unsafe_allow_html=True)
            st.info(joke['joke'])

# Streamlit app
st.title('Joke Generator')

jokes = fetch_jokes()

st.write("Here are some jokes for you!")

display_jokes(jokes)
