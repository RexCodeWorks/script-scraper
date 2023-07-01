from google.cloud import speech


def run_quickstart(speech_file_gcs_uri: str) -> speech.LongRunningRecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=speech_file_gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        sample_rate_hertz=48000,
        audio_channel_count=2,
        language_code="en-US",
        enable_word_time_offsets=True,  # timestamp information
    )

    # Detects speech in the audio file using LongRunningRecognize with GCS URI
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result()

    print("Transcription results:")
    print(response)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

if __name__ == "__main__":
    gcs_audio_uri = "gs://shotify-speech-to-text-audio/audio_file.wav"
    run_quickstart(gcs_audio_uri)
