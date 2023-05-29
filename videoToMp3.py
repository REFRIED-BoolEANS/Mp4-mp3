from moviepy.editor import VideoFileClip

def convert_to_mp3(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.audio.write_audiofile(output_file)

input_file = "I:\sleepingMusic.mp4"
output_file = "I:\output.mp3"

convert_to_mp3(input_file, output_file)