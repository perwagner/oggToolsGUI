from tkinter import *
from tkinter.filedialog import *
import os, sys, ntpath, shutil

class App:
    def __init__(self, master):
        self.label_bg_color = 'LightSteelBlue1'
        self.button_activebackground = 'light green'

        self.source_file = 'no source file'
        self.source_filename = 'NoSourcefileSelected'
        self.dest_audio_file = "no audio file name"
        self.dest_video_file = "no video file name"
        self.initial_dir = "/home/perwagner/Videos"

        frame = Frame(master, background = self.label_bg_color)
        frame.grid()

        Label(frame, text = "Directory:", bg = self.label_bg_color, width = 20, anchor = W).grid(row = 0, column = 0)

        self.lab_dir = Label(frame, text =self.initial_dir, bg = self.label_bg_color, width = 20, anchor = W)
        self.lab_dir.grid(row = 0, column = 1)

        Label(frame, text = "Source filename:", bg = self.label_bg_color, width = 20, anchor = W).grid(row = 1, column = 0)

        self.lab_source = Label(frame, text =self.source_file, bg = self.label_bg_color, width = 20, anchor = W)
        self.lab_source.grid(row = 1, column = 1)

        Label(frame, text = "Dest. audio filename:", bg = self.label_bg_color, width = 20, anchor = W).grid(row = 2, column = 0)
        Label(frame, text = "Dest. git video filename:", bg = self.label_bg_color, width = 20, anchor = W).grid(row = 3, column = 0)
        self.lab_dest_audio = Label(frame, text = self.dest_audio_file, bg = self.label_bg_color, width = 20, anchor = W)
        self.lab_dest_audio.grid(row = 2, column = 1)
        self.lab_dest_video = Label(frame, text = self.dest_video_file, bg = self.label_bg_color, width = 20, anchor = W)
        self.lab_dest_video.grid(row = 3, column = 1)

        #Buttons
        self.but_add_file = Button(frame, text = 'Add OGV file', activebackground = self.button_activebackground, command = self.add_file)
        self.but_add_file.grid(row = 5, column = 0)
        self.but_add_file = Button(frame, text = 'Convert file', activebackground = self.button_activebackground, command = self.oggSplit)
        self.but_add_file.grid(row = 5, column = 1)

        #self.but_test = Button(text = "TEST", command = self.test)
        #self.but_test.grid(row = 10, column = 0)

    def test(self):
        root, ext = os.path.splitext(self.source_filename)
        print(root)
        print(ext)

    def add_file(self):
        self.source_file = askopenfilename(initialdir = '/home/perwagner/Videos')
        head, tail = self.path_leaf(self.source_file)
        self.initial_dir = head
        self.source_filename = tail

        root, ext = os.path.splitext(self.source_filename)

        self.lab_source.config(text = self.source_filename)
        self.lab_dir.config(text = self.initial_dir)
        self.lab_dest_audio.config(text = root + "_audio" + ext)
        self.lab_dest_video.config(text = root + "_video" + ext)


    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return head, tail


    def oggSplit(self):
        command = 'oggSplit ' + self.source_file
        os.system(command)

        #Python puts the files in the GUI's directory, thus need to move them
        #to the source directory before proceeding
        files = os.listdir(os.getcwd())
        for file in files:
            if 'vorbis' in file or 'theora' in file or 'unknown_' in file:
                src_file = os.getcwd() + "/" + file
                shutil.move(src_file, self.initial_dir)

        #Renaming file names
        files = os.listdir(self.initial_dir)
        source_filename, ext = os.path.splitext(self.source_filename)


        for file in files:
            root, ext = os.path.splitext(file)
            filename=file
            file = self.initial_dir + "/" + file
            if "theora_" in file:
                os.rename(file, self.initial_dir + "/" + source_filename + "_video" + ext)
            if "vorbis_" in file:
                os.rename(file, self.initial_dir + "/" + source_filename + "_audio" + ext)
            if "unknown_" in file:
                os.rename(file, self.initial_dir + "/" + source_filename + "_unknown" + ext)




# Main program
root = Tk()
root.title("pyOggTools")
app = App(root)

root.mainloop()
