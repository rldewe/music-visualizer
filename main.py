from pydub import AudioSegment
import simpleaudio as sa
import librosa
import librosa.display
import matplotlib.pyplot as plt
import threading

# === Step 1: Load your audio ===
audio_path = "sample_audio.mp3"

# Load with pydub for playback
song = AudioSegment.from_file(audio_path, format="mp3")

# Load with librosa for analysis
y, sr = librosa.load(audio_path)

# === Step 2: Function to play the song ===
def play_song():
    play_obj = sa.play_buffer(
        song.raw_data,
        num_channels=song.channels,
        bytes_per_sample=song.sample_width,
        sample_rate=song.frame_rate
    )
    play_obj.wait_done()

# === Step 3: Play song in background thread ===
thread = threading.Thread(target=play_song)
thread.start()

# === Step 4: Plot waveform ===
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr, color='mediumseagreen')
plt.title("Waveform of Music (playing...)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Wait for song to finish before exiting
thread.join()
