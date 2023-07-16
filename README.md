# Smart Voice Assistant
This codebase uses ASR (Automatic Speech Recognition) model for speech transcription and query a LLM model to generate a response. The generated response is then passed to the TTS (text-to-speech) model for speech synthesis.

Here, the smart voice assistant doesn't use wake-word detection techniques. It just uses a pre-trained Whisper Model for transcribing spoken user queries.

This project is hosted on HuggingFace Spaces: [Live Demo of Smart Voice Assistant](https://huggingface.co/spaces/heliosbrahma/voice-assistant).
<br>
## How to run it locally:-
To run this app locally, first clone this repo using `git clone`.<br><br>
Now, install all libraries by running the following command in the terminal:<br>
```python
pip install -r requirements.txt
```
<be><br>
Now, run the app from the terminal:<br>
```python
gradio app.py
```
