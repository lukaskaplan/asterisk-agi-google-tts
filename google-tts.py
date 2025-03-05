#!/usr/bin/env python3

"""
Google Text-to-Speech API AGI script for Asterisk.
Author: Lukas Kaplan
GitHub: https://github.com/lukaskaplan/asterisk-agi-google-tts
License: MIT

This script converts text to speech using Google TTS and saves the output as a WAV file (8kHz, mono PCM).
It is optimized for use as an AGI script in Asterisk.

Usage (in Asterisk dialplan):
    same => n,AGI(google-tts.py,"Text to synthesize","/path/to/output.wav")

Requirements:
    - requests (pip install requests)
    - A valid Google TTS API key (set as GOOGLE_TTS_API_KEY env variable or directly in the script)
"""

import requests
import base64
import sys
import os

# Configuration
DEFAULT_API_KEY = None  # Set your api key here if needed
API_KEY = os.getenv("GOOGLE_TTS_API_KEY", DEFAULT_API_KEY)
LANGUAGE = "cs-CZ"
SAMPLE_RATE = 8000  # 8kHz, best for Asterisk
AUDIO_FORMAT = "LINEAR16"   # Uncompressed WAV, best for Asterisk

def synthesize_speech(text: str, output_file: str):
    """
    Sends a request to Google Text-to-Speech API to synthesize speech from text.

    :param text: The text to be converted to speech.
    :param output_file: Path to the output WAV file.
    :return: Exit code (0 = success, 1 = failure)
    """
    if not API_KEY:
        sys.exit(1)  # Exit silently (Asterisk AGI should handle the error)

    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"
    payload = {
        "input": {"text": text},
        "voice": {"languageCode": LANGUAGE, "ssmlGender": "NEUTRAL"},
        "audioConfig": {"audioEncoding": AUDIO_FORMAT, "sampleRateHertz": SAMPLE_RATE}
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            response_json = response.json()
            audio_content = base64.b64decode(response_json["audioContent"])

            # Save to file
            with open(output_file, "wb") as audio_file:
                audio_file.write(audio_content)

            sys.exit(0)  # Success
        else:
            sys.exit(1)  # API request failed
    except Exception:
        sys.exit(1)  # Handle network issues

def main():
    """Main function to process AGI input arguments."""
    if len(sys.argv) != 3:
        sys.exit(1)  # Incorrect usage, Asterisk will handle the error

    text = sys.argv[1]
    output_file = sys.argv[2]

    synthesize_speech(text, output_file)

if __name__ == "__main__":
    main()