import requests
from decouple import config


ELEVEN_LABS_API_KEY= config("ELEVEN_LABS_API_KEY")
ELEVEN_LABS_CHARLIE_VOICE_ID=config("ELEVEN_LABS_CHARLIE_VOICE_ID")


# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
    # Define data
    body={
        "text": message,
        "voice_settings": {
            "stability":0.1,
            "similarity_boost":0.1
        }
    }
    # Define voice
    voice_agent = ELEVEN_LABS_CHARLIE_VOICE_ID
    # Constructing headers and endpoint
    headers= {"xi-api-key":ELEVEN_LABS_API_KEY,"Content-Type":"application/json","accept":"audio/mpeg"}
    endpoint= f"https://api.elevenlabs.io/v1/text-to-speech/{voice_agent}"
    # Send request
    try:
        response= requests.post(endpoint,json=body,headers=headers)
    except Exception as e:
        print(e)
        return
    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return