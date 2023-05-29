from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_to_mp3():
    input_file = input_entry.get()
    output_file = output_entry.get()
    
    clip = VideoFileClip(input_file)
    clip.audio.write_audiofile(output_file)

def browse_input_file():
    filename = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    input_entry.delete(0, END)
    input_entry.insert(0, filename)

def browse_output_file():
    filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
    output_entry.delete(0, END)
    output_entry.insert(0, filename)

# Create the main window
window = Tk()
window.title("Video to MP3 Converter")

# Create input file label and entry
input_label = Label(window, text="Input File:")
input_label.pack()
input_entry = Entry(window, width=50)
input_entry.pack()
browse_input_button = Button(window, text="Browse", command=browse_input_file)
browse_input_button.pack()

# Create output file label and entry
output_label = Label(window, text="Output File:")
output_label.pack()
output_entry = Entry(window, width=50)
output_entry.pack()
browse_output_button = Button(window, text="Browse", command=browse_output_file)
browse_output_button.pack()

# Create convert button
convert_button = Button(window, text="Convert", command=convert_to_mp3)
convert_button.pack()

# Start the main loop
window.mainloop()
