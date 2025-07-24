# app.py

import streamlit as st
import whisper
import os

def save_uploaded_file(uploaded_file):
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)

def main():
    st.set_page_config(page_title="Kelpath - AI Interview Feedback", layout="centered")
    st.title("🎤 Kelpath - AI Interview Feedback System")

    st.markdown("#### Upload your audio response:")
    uploaded_file = st.file_uploader("Choose an audio file (mp3/wav)", type=["mp3", "wav"])

    if uploaded_file:
        filepath = save_uploaded_file(uploaded_file)
        st.success("✅ Audio uploaded successfully")

        st.markdown("### 🔍 Transcribing...")

        model = whisper.load_model("base")
        result = model.transcribe(filepath)
        transcript = result["text"]

        st.markdown("### 📝 Transcription:")
        st.write(transcript)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    main()
