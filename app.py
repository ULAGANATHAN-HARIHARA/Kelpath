# app.py

import streamlit as st

def main():
    st.set_page_config(page_title="Kelpath - AI Interview Feedback", layout="centered")
    st.title("🎤 Kelpath - AI Interview Feedback System")
    st.write("Upload your audio or speak directly, and let AI give you feedback on your answer!")

if __name__ == "__main__":
    main()
