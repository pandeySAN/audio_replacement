from google.cloud import speech

def transcribe_audio(audio):
    client = speech.SpeechClient()

    with open(audio, "rb") as f:
        sound = f.read()

    audio_data = speech.RecognitionAudio(content=sound)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    result = client.recognize(config=config, audio=audio_data)

    transcript = ""
    for r in result.results:
        transcript += r.alternatives[0].transcript

    return transcript
