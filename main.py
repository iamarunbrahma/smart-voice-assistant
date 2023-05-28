import whisper
import gradio as gr 
import openai
from TTS.api import TTS
import subprocess
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
model_name = TTS.list_models()[9]
tts = TTS(model_name)
model = whisper.load_model('medium')

def run_ffmpeg_command():
    command = ['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '1', '-q:a', '9', '-acodec', 'libmp3lame', 'output.wav']
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


def voice_chat(user_voice):
    openai.api_key = OPENAI_API_KEY
    messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
    ]
             
    user_message = model.transcribe(user_voice)["text"]
    messages.append(
        {"role": "user", "content": user_message},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )    
    reply = chat.choices[0].message.content
    
    messages.append({"role": "assistant", "content": reply})
    tts.tts_to_file(text=reply, file_path="output.wav")
    return(reply, "output.wav")

# run_ffmpeg_command()
    
gr.Interface(
    title = 'Smart Voice Assistant',
    description = 'Use this gradio app interface to get answers for all your queries in both text and speech format. \
    Just communicate your queries in speech format and this app will take care of the rest.',
    fn=voice_chat, 
    inputs=[
        gr.Audio(source="microphone", label="Input Voice", type="filepath")        
    ],
    outputs=[
        gr.Textbox(label="Summarized Answer"),
        gr.Audio(label="Output Speech", type="filepath")
    ]).launch()