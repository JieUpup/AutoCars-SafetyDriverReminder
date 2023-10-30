from gtts import gTTS
import os
import platform


class AudioSynthesisModule:

    def __init__(self):
        self.supported_languages = ['en', 'es', 'fr', 'de']  # and others, based on gTTS's capabilities

    def text_to_audio(self, text, language='en', output_file='output.mp3'):
        """
        Converts the provided text into an audio file.

        Parameters:
        - text (str): The text to convert.
        - language (str): The language of the text. Default is 'en' (English).
        - output_file (str): The name of the output audio file.

        Returns:
        str: The name of the output audio file.
        """
        if language not in self.supported_languages:
            raise ValueError(
                f"Unsupported language '{language}'. Supported languages are {', '.join(self.supported_languages)}")

        try:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(output_file)
            return output_file
        except Exception as e:
            print(f"Error converting text to audio: {e}")
            return None

    def play_audio(self, audio_file):
        """
        Plays the provided audio file.

        Parameters:
        - audio_file (str): The name of the audio file to play.
        """
        try:
            if platform.system() == "Windows":
                os.system(f"start {audio_file}")
            elif platform.system() == "Linux":
                os.system(f"xdg-open {audio_file}")
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open {audio_file}")
            else:
                print("Unsupported OS.")
        except Exception as e:
            print(f"Error playing audio: {e}")


if __name__ == "__main__":
    audio_module = AudioSynthesisModule()

    # Sample text for testing
    text_response = "Please be cautious. A collision might be possible ahead."

    # Convert text to audio and play it
    output_file = audio_module.text_to_audio(text_response)
    if output_file:
        audio_module.play_audio(output_file)
