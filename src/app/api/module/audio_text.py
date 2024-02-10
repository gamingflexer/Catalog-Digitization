# from whisper_jax import FlaxWhisperPipline
# import jax.numpy as jnp
import whisper
print(whisper.__file__)
from openai import OpenAI
from module.config import OPENAI_API_KEY
import os

client = OpenAI()
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


# def whisper_pipeline_tpu(audio):
#     pipeline = FlaxWhisperPipline("openai/whisper-large-v3", dtype=jnp.bfloat16, batch_size=16)
#     text = pipeline(audio)
#     return text


     
def whisper_pipeline(audio_path):
    model = whisper.load_model("medium")
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")
    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    # print the recognized text
    print(result.text)
    return result.text





def whisper_openai(audio_path):
   audio_file= open(audio_path, "rb")
   transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
   )
   return transcript

whisper_pipeline()