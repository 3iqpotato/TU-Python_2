

import numpy as np
from scipy.io import wavfile

class MusicGenerator:
    def __init__(self, sampling_rate):
        self.sampling_rate = sampling_rate

    def generate_sine_wave(self, frequency, duration, amplitude):
        num_samples = int(self.sampling_rate * duration)
        time = np.linspace(0, duration, num_samples, endpoint=False)
        audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)
        return audio_signal

    def generate_music(self, notes):
        composed_music = np.array([])
        for note in notes:
            note_length = note[2]
            audio_signal = self.generate_sine_wave(note[1], note_length, 0.2)
            composed_music = np.append(composed_music, audio_signal)
        return composed_music

    def save_signal_to_wav(self, filename, signal):
        max_amplitude = np.max(np.abs(signal))
        normalized_signal = signal / max_amplitude
        wavfile.write(filename, self.sampling_rate, normalized_signal)

def main():
    sampling_rate = 44100
    music_generator = MusicGenerator(sampling_rate)

    # Define musical notes with frequency, duration, and amplitude
    notes = [
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('B4', 493.88, 0.5),   # B in the 4th octave
        ('D5', 587.33, 0.5),   # D in the 5th octave
        ('C5', 523.25, 0.5),   # C in the 5th octave
        ('A4', 440.00, 1),   # A in the 4th octave
    ]

    # Generate and save the music
    composed_music = music_generator.generate_music(notes)
    music_generator.save_signal_to_wav("composed_music.wav", composed_music)

if __name__ == "__main__":
    main()
