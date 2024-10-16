import openai
import os

# Azure OpenAI API Key and Endpoint
key = "22ec84421ec24230a3638d1b51e3a7dc"
url = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

openai.api_type = "azure"
openai.api_key = key
openai.api_base = url.split('/openai/')[0]
openai.api_version = "2024-08-01-preview"

def correct_transcription(text):
    response = openai.ChatCompletion.create(
        engine="gpt-4o",
        messages=[
            {"role": "system", "content": "You help fix text."},
            {"role": "user", "content": text}
        ]
    )

    corrected = response['choices'][0]['message']['content']
    return corrected
