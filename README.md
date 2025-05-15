# Whisper Transcription Project
## Overview
This project compares transcriptions from Hugging Face Whisper models (base and small) using a Gradio GUI. Users can upload MP3 files (up to 30 seconds) to see transcriptions from both models side by side. A presentation summarizing the project, methodology, and results is included.

## Files
mp3_to_text_Whisper_Transcription.py: Main Python script for the Gradio app.

mp3_to_text_Whisper_Transcription.ipynb: Main Notebook

SAHIL_SINGH_MP3_TO_TEXT.pptx: Compiled presentation (slides).

## Setup
Install Python: Ensure Python 3.8+ is installed.
Create Virtual Environment (recommended):python -m venv whisper_env
source whisper_env/bin/activate  # Windows: whisper_env\Scripts\activate

Install Dependencies:
```Install PyTorch (CPU version):pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cpu```

Install other libraries:
```pip install transformers gradio```

Install FFmpeg:
FFmpeg is required for MP3 processing. On Windows, add it to PATH (e.g., C:\ffmpeg\bin).

## Usage
Run the Application:python mp3_to_text_Whisper_Transcription.py
This launches a Gradio interface (e.g., http://127.0.0.1:7860).
Upload an MP3 File:
Upload a 30-second MP3 file via the Gradio GUI.
Click "Transcribe" to see results from both Whisper base and small models.

## Results
Clear Audio: Both models produce similar results (e.g., LibriSpeech clips).

Unclear Audio: Small model performs better (e.g., noisy background speech).

See the presentation (Whisper_Transcription_Presentation.pdf) for a detailed comparison table and slides.

## Presentation
The project includes a 5-slide presentation:

Introduction and methodology.

Results with a comparison table.

Conclusion and future work.

## Limitations
Currently processes MP3 files up to 30 seconds.

Future work: Extend to longer files, add quantitative metrics (e.g., Word Error Rate).
