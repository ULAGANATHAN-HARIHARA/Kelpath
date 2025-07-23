
import streamlit as st
from audiorecorder import audiorecorder

# Title
st.title("🎙️ AI Interview Feedback - Voice Input")

# Record Audio
st.subheader("Step 1: Record Your Interview Answer")
audio = audiorecorder("🔴 Start Recording", "🔁 Stop Recording")

if len(audio) > 0:
    st.audio(audio.tobytes(), format="audio/wav")
    # Save to file
    with open("temp_audio.wav", "wb") as f:
        f.write(audio.tobytes())
    st.success("✅ Audio saved as temp_audio.wav")
