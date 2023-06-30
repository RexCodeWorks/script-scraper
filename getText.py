from google.cloud import speech_v1p1beta1 as speech
import io


def transcribe_file(speech_file):
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # audio_channel_count=2,             # Update this line
        language_code="en-EN",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == "__main__":
    audio_file_path = "audio_file.m4a"
   
