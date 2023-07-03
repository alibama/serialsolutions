import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_css(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all CSS styles from the page
    css_styles = soup.find_all('style')

    # Consolidate all CSS styles into a single string
    consolidated_css = '\n'.join([style.get_text() for style in css_styles])

    return consolidated_css

def save_to_file(css, output_file):
    with open(output_file, 'w') as f:
        f.write(css)

# Streamlit app
st.title("CSS Extractor")

# User input: URL and output file path
url = st.text_input("Enter the URL of the web page:")
output_file = st.text_input("Enter the output file path (e.g., styles.css):")

if st.button("Extract CSS"):
    if url and output_file:
        # Extract CSS styles from the web page
        try:
            css = extract_css(url)

            # Save the CSS styles to a file
            save_to_file(css, output_file)

            st.success("CSS styles extracted and saved successfully!")
        except Exception as e:
            st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter a URL and output file path.")

