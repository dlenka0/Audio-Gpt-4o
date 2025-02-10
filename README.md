# Audio Translation with OpenAI

A powerful Python application that translates audio content into different languages using OpenAI's Whisper and GPT models. The application first transcribes the audio to text and then translates it while maintaining the original context and meaning.

## Features

- 🎙️ Audio transcription using OpenAI's Whisper model
- 🌐 Text translation to any language using GPT-4
- 📝 Saves both original transcription and translation
- 🔍 Maintains context and technical terminology
- 🚀 Easy to use and extend

## Requirements

- Python 3.10+
- OpenAI API key
- Input audio in WAV format (can be converted from other formats)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/deepak-lenka/Audio-Gpt-4o.git
cd Audio-Gpt-4o
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your audio file (WAV format) in the project directory as `input.wav`

2. Run the translator:
```bash
python voice_translator.py
```

3. Find the results in the `translations` directory:
   - `input_original.txt`: Original transcription
   - `input_hindi.txt`: Translated text (default: Hindi)

## Customization

To translate to a different language, modify the `target_language` parameter when calling `translate_audio()` in `voice_translator.py`:

```python
translate_audio("input.wav", target_language="French")  # or any other language
```

## Audio Format Conversion

If your audio is in a different format, you can convert it to WAV using ffmpeg:
```bash
ffmpeg -i input.mp3 input.wav  # Replace mp3 with your audio format
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenAI for providing the Whisper and GPT APIs
- The open-source community for various tools and libraries used in this project
