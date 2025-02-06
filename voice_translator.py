import os
import json
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def encode_audio_file(file_path):
    """
    Encode an audio file to base64
    """
    with open(file_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode('utf-8')

def process_audio_with_gpt_4o(audio_file_path, target_language):
    """
    Process audio using OpenAI's Whisper and GPT models
    
    Args:
        audio_file_path (str): Path to the audio file
        target_language (str): Target language for translation
    
    Returns:
        tuple: (transcription, translation)
    """
    client = OpenAI()

    try:
        # First, transcribe the audio
        with open(audio_file_path, 'rb') as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        # Then, translate the transcription
        translation = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a professional translator. Translate the following text to {target_language} while maintaining the original tone and context."}, 
                {"role": "user", "content": transcription.text}
            ]
        )

        return transcription.text, translation.choices[0].message.content

    except Exception as e:
        print(f"Error: {e}")
        return None, None

def translate_audio(input_file, target_language="Hindi"):
    """
    Translate audio file to target language
    
    Args:
        input_file (str): Path to input audio file
        target_language (str): Target language for translation
    """
    # Process the audio for translation
    original_text, translated_text = process_audio_with_gpt_4o(input_file, target_language)
    
    if original_text and translated_text:
        # Save the translations
        output_dir = "translations"
        os.makedirs(output_dir, exist_ok=True)
        
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        original_output = f"{output_dir}/{base_name}_original.txt"
        translation_output = f"{output_dir}/{base_name}_{target_language.lower()}.txt"
        
        # Save original transcription
        with open(original_output, "w", encoding="utf-8") as f:
            f.write(original_text)
        print(f"Original transcription saved to: {original_output}")
        
        # Save translation
        with open(translation_output, "w", encoding="utf-8") as f:
            f.write(translated_text)
        print(f"Translation saved to: {translation_output}")
    else:
        print("Translation failed. Please check the error messages above.")

if __name__ == "__main__":
    # Example usage
    input_file = "input.wav"  # Replace with your input audio file
    translate_audio(input_file, target_language="Hindi")
