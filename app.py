import streamlit as st
from transcribe import transcribe_audio
from correct_transcription import correct_transcription
from text_to_speech import text_to_speech
from video_utils import extract_audio, replace_audio_in_video
from moviepy.editor import VideoFileClip

st.title("Replace Audio in Video with AI")
video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video:
    st.video(video)

    with open("my_video.mp4", "wb") as file:
        file.write(video.read())
    
    st.success("Video uploaded!")

    # Step 1: Get the audio from the video
    my_audio = extract_audio("my_video.mp4")
    st.success("Got the audio!")

    # Step 2: Convert the audio to text
    my_text = transcribe_audio(my_audio)
    st.text_area("Original Text", my_text)

    # Step 3: Fix the text
    fixed_text = correct_transcription(my_text)
    st.text_area("Fixed Text", fixed_text)

    # Step 4: Make the robot voice
    ai_voice = "robot_voice.wav"
    text_to_speech(fixed_text, ai_voice)
    st.success("AI voice ready!")

    # Step 5: Swap out the audio in the video
    replace_audio_in_video("my_video.mp4", ai_voice)
    st.success("New video with AI voice ready!")
    
    st.video("my_final_video.mp4")
    with open("my_final_video.mp4", "rb") as final_vid:
        st.download_button("Download New Video", final_vid, file_name="my_final_video.mp4")
