## AI Audio Replacement for Videos
This project replaces the audio of a video file with AI-generated speech. It extracts the original
audio, converts it into text, corrects the text using AI, and then generates new audio. The
AI-generated audio is synced with the original video to create a final output video.
## Features
- Upload a video file (mp4, avi, mov)
- Extract the audio from the video
- Transcribe the audio to text using Google Cloud's Speech-to-Text API
- Correct the transcription using Azure's GPT-4o model
- Generate AI-based speech from the corrected text using Google Cloud's Text-to-Speech API
- Replace the original audio with the new AI-generated audio in the video
## Setup
### Prerequisites
1. Python 3.8+
2. Install the required libraries:
 ```bash
 pip install streamlit moviepy google-cloud-speech google-cloud-texttospeech openai
 ```
### APIs Used
- **Google Cloud Speech-to-Text API**: For converting audio to text.
- **Azure OpenAI GPT-4o API**: For correcting the transcribed text.
- **Google Cloud Text-to-Speech API**: For converting corrected text into audio.
### API Key Setup
- **Google Cloud API Key**: You need to set up your Google Cloud credentials for Speech-to-Text
and Text-to-Speech.
- **Azure OpenAI API Key**: You need to get your API key and endpoint for Azure's GPT-4o model.
## How to Run the App
1. Clone this repository.
2. Run the Streamlit app:
 ```bash
 streamlit run app.py
 ```
3. Upload a video, and the app will process it.
## How It Works
1. **Upload Video**: The user uploads a video file (supported formats: mp4, avi, mov).
2. **Extract Audio**: The app extracts the audio from the video.
3. **Transcribe Audio**: The audio is transcribed into text using Google Cloud's Speech-to-Text API.
4. **Correct Transcription**: The transcribed text is corrected using Azure?s GPT-4o AI model.
5. **Generate AI Voice**: The corrected text is converted into speech using Google Cloud's
Text-to-Speech API.
6. **Replace Audio**: The new AI-generated audio is placed back into the original video.
7. **Download Final Video**: The final video with the new audio is available for download.
## File Structure
```
??? app.py # Main Streamlit app
??? transcribe.py # Audio transcription function
??? correct_transcription.py # Transcription correction function
??? text_to_speech.py # Text-to-Speech function
??? video_utils.py # Video processing utilities (extract/replace audio)
??? README.md # This file
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.