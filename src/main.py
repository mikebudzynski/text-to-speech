import azure.cognitiveservices.speech as speechsdk
from config import *

text = ""

# Read the text from the input file
with open(INPUT_FILE_PATH, "r") as file:
   text = file.read()

speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)

# Note: the voice setting will not overwrite the voice element in input SSML.
speech_config.speech_synthesis_voice_name = SPEECH_VOICE
# Don't play the audio through the speakers
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=False, filename=OUTPUT_FILE_PATH)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

result = None

if "ssml" in INPUT_FILE_PATH or INPUT_FILE_PATH.endswith(".xml"):
    # Generate speech from SSML
    result = speech_synthesizer.speak_ssml_async(text).get()
else:
    # Generate speech from plain text
    result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfully synthesized speech!")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))