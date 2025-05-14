# asterisk-agi-google-tts

Google Text-to-Speech (TTS) AGI Script for Asterisk

This script uses Google Cloud Text-to-Speech API to convert text into speech and save it as a WAV file (8kHz, LINEAR16), making it suitable for use with Asterisk AGI.

## Features

- Uses Google Cloud Text-to-Speech API
- Generates **8kHz LINEAR16 WAV** files for Asterisk
- Works as an **AGI script** in Asterisk
- Supports **environment variable-based API key management**
- Fast and efficient

## Installation

### Prerequisites

- **Python 3** (tested with Python 3.7+)
- `requests` library
- A **Google Cloud API Key** with access to the Text-to-Speech API

### Install dependencies

```sh
pip install requests
```

## Usage

### 1️⃣ Set up the API Key

You can configure the API key in two ways:

**Option 1: Use an environment variable (recommended)**

```sh
export GOOGLE_TTS_API_KEY="your-google-api-key"
```

**Option 2: Set it inside the script (not recommended for security reasons)** Edit the script and replace:

```python
DEFAULT_API_KEY = "your-google-api-key"
```

### 2️⃣ Run the script manually

```sh
python google_tts.py "Hello, this is a test" /path/to/output.wav
```

### 3️⃣ Use as an Asterisk AGI Script

#### Copy the script to Asterisk AGI directory:

```sh
cp google_tts.py /var/lib/asterisk/agi-bin/google_tts.py
chmod +x /var/lib/asterisk/agi-bin/google_tts.py
```

#### Example Asterisk Dialplan (extensions.conf):

```asterisk
exten => 1234,1,Answer()
same  => n,AGI(google_tts.py,"Hello, welcome to our system","/var/lib/asterisk/sounds/custom/greeting.wav")
same  => n,Playback(custom/greeting)
same  => n,Hangup()
```

### 4️⃣ Unset API Key (if needed)

#### Linux/macOS:

```sh
unset GOOGLE_TTS_API_KEY
```

## License

MIT License. Feel free to use and modify as needed.

## Repository

GitHub: [github.com/lukaskaplan/asterisk-agi-google-tts](https://github.com/lukaskaplan/asterisk-agi-google-tts)

## Author

- Lukas Kaplan
- GitHub: [lukaskaplan](https://github.com/lukaskaplan)

