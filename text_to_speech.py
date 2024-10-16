from google.cloud import texttospeech

def text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-J",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    
    config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=config
    )

    with open(output_file, "wb") as f:
        f.write(response.audio_content)
