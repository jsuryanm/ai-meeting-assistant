from src.utils.whisper_utils import transcribe_audio
from src.utils.main_utils import clean_transcript
from src.core.assistant import generate_meeting_minutes


def process_meeting(audio_file):
    print("Transcribing audio...")
    transcript = transcribe_audio(audio_file)
    print("Cleaning transcript...")
    cleaned = clean_transcript(transcript)
    print("Generating meeting minutes...")
    minutes = generate_meeting_minutes(cleaned)
    return minutes


if __name__ == "__main__":

    audio_file = "sample-meeting.wav"
    output = process_meeting(audio_file)
    print("\n===== MEETING OUTPUT =====\n")
    print(output)