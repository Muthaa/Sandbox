import os
import sounddevice
import numpy as np
import time
from scipy.io.wavfile import write
from pydub import AudioSegment
from datetime import datetime

def record_audio(sample_rate):
    """
    Function to continuously record audio until a keyboard key is pressed.
    Args:
    - sample_rate (int): The sample rate for recording.
    Returns:
    - numpy.ndarray: Recorded audio data.
    """
    print("Recording... (Press Ctrl+C to stop)")
    recorded_voice = []
    def callback(indata, frames, time, status):
        if status:
            print(status)
        recorded_voice.append(indata.copy())
    
    with sounddevice.InputStream(samplerate=sample_rate, callback=callback):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    
    audio_data = np.concatenate(recorded_voice)
    print("Recording stopped.")
    return audio_data

def save_audio(sample_rate, audio_data):
    """
    Function to save audio data as a WAV file with an increasing index in the filename.
    Args:
    - sample_rate (int): The sample rate of the audio data.
    - audio_data (numpy.ndarray): The audio data to be saved.
    Returns:
    - str: Filename of the saved WAV file.
    """
    index = 0
    while True:
        filename = f"rec_V2_{index:02}.wav"
        if not os.path.exists(filename):
            audio_segment = AudioSegment(
                audio_data.tobytes(),
                frame_rate=sample_rate,
                sample_width=audio_data.dtype.itemsize,
                channels=2
            )
            # Add metadata
            audio_segment.export(filename, format="wav", tags={
                "title": filename,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                # Add other metadata fields as needed
            })
            print(f"Audio saved as {filename}")
            return filename
        index += 1

def main():
    sample_rate = 44100
    audio_data = record_audio(sample_rate)
    save_audio(sample_rate, audio_data)

if __name__ == "__main__":
    main()


