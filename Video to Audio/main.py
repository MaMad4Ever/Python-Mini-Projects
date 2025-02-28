import moviepy.editor as mp

clip = mp.VideoFileClip(r"Video File")

clip.audio.write_audiofile(r"Audio File")
