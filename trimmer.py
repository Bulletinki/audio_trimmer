import os
from pydub import AudioSegment
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# change working directory to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# open a file dialog to choose an audio file
Tk().withdraw()
audio_file = askopenfilename()

# read in the audio file
audio = AudioSegment.from_file(audio_file)

# check the file size in megabytes
file_size_mb = os.path.getsize(audio_file) / (1024 * 1024)

# if the file size is greater than 10 MB, trim the file
if file_size_mb > 10:
    # calculate the duration of the audio file to trim
    duration_to_trim = (file_size_mb - 10) / file_size_mb * len(audio)

    # trim the audio file
    trimmed_audio = audio[duration_to_trim:]

    # export the trimmed audio file to the same directory with the same name as the input file except with "TRIMMED_" as the prefix
    output_file = os.path.join(os.path.dirname(audio_file), "TRIMMED_" + os.path.basename(audio_file))
    trimmed_audio.export(output_file, format="mp3")
