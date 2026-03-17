import gradio as gr
import tempfile 
import os 

from src.utils.whisper_utils import transcribe_audio
from src.utils.main_utils import clean_transcript
from src.core.assistant import generate_meeting_minutes

def process_meeting(audio_file):
    if audio_file is None:
        "Please upload or record the audio"

    raw_transcript = transcribe_audio(audio_file)
    cleaned_transcript = clean_transcript(raw_transcript)
    meeting_minutes = generate_meeting_minutes(cleaned_transcript)
    return cleaned_transcript,meeting_minutes

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("AI Meeting Assistant")
    gr.Markdown("Record or upload meeting audio and get insant notes")

    with gr.Row():
        audio_input = gr.Audio(sources=["microphone","upload"],
                               type="filepath",
                               label="Upload or record audio")
        
        
        process_button = gr.Button("Generate Meeting Minutes")
        with gr.Row():
            transcript_box = gr.Textbox(label="Transcript",
                                        lines=15)

        with gr.Row():
            minutes_box = gr.Textbox(label="Meeting minutes",
                                     lines=25)
        
        process_button.click(fn=process_meeting,
                             inputs=audio_input,
                             outputs=[transcript_box,minutes_box])

if __name__ == "__main__":
    demo.launch(share=True)