import png
import glob
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile


# Change this parameters if you want
window_time = 20
picture_height = 40
audio_max_lenght = 5500
sample_rate = 8000
number_of_levels = 256
for filename in glob.iglob('wavs/*.wav'):

    fs, wave = wavfile.read(filename)  # load the data
    num_samples = len(wave)
    samples_per_window = int((sample_rate * window_time/1000.0))
    max_windows = audio_max_lenght*(sample_rate/1000)/window_time

    # Array of arrays
    energy_level_per_windows = []
    all_numbers = []
    for window_offset in range(max_windows):
        audio_windows = num_samples/window_time
        fourier = fft(wave[window_offset:window_offset + samples_per_window])
        # Remove Fourier Transform Symmetries, adds no information
        fourier = fourier[:len(fourier) / 2]
        # Gets absolute value (magnitude)
        fourier = abs(fourier)
        # Gets values in db if needed later
        fourier = 20 * np.log10(fourier)

        bandwidth = len(fourier)/picture_height
        column = []
        for pixel in range(picture_height):
            if window_offset > audio_windows:
                average_level = "w"
            else:
                average_level = np.mean(fourier[pixel*bandwidth:(pixel+1)*bandwidth])
                all_numbers.append(average_level)
            column.append(average_level)


        energy_level_per_windows.append(column)

    top = max(all_numbers)
    bot = min(all_numbers)

    matrix = []
    for line in energy_level_per_windows:
        new_line = []
        for element in line:
            if element is "w":
                new_line.append(0)
            else:
                new_line.append(int(((element-bot)/(top-bot))*255))
        matrix.append(new_line)

    audio = filename[5:11]
    png.from_array(matrix, 'L').save("pngs/"+audio+".png")
