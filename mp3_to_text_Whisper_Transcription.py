#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gradio as gr
from transformers import pipeline

def load_models():
    base_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    small_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    return base_pipe, small_pipe

def transcribe(audio, model_name):
    base_pipe, small_pipe = load_models()
    pipe = base_pipe if model_name == "Base" else small_pipe
    result = pipe(audio)
    return result["text"]

def process_audio(audio):
    if audio is None:
        return "No audio uploaded.", ""
    base_text = transcribe(audio, "Base")
    small_text = transcribe(audio, "Small")
    return base_text, small_text

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Hugging Face Whisper Transcription")
    audio_input = gr.Audio(type="filepath", label="Upload MP3")
    submit_button = gr.Button("Transcribe")
    base_output = gr.Textbox(label="Base Model Transcription")
    small_output = gr.Textbox(label="Small Model Transcription")
    submit_button.click(process_audio, inputs=audio_input, outputs=[base_output, small_output])

if __name__ == "__main__":
    demo.launch()


# In[ ]:





# In[ ]:





# In[ ]:




