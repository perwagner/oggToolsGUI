from tkinter import *
from tkinter.filedialog import *
import os, sys, ntpath, shutil

class App:
    def __init__(self, master):
        self.source_file = 'no source file'
        self.source_filename = 'NoSourcefileSelected'
        self.dest_audio_file = "no audio file name"
        self.dest_video_file = "no video file name"
        self.initial_dir = "/home/perwagner/Videos"

        frame = Frame(master)
        frame.grid()

        self.but_add_file = Button(text = 'Add OGV file', command = self.add_file)
        self.but_add_file.grid(row = 5, column = 0)

        Label(text = "Directory:").grid(row = 0, column = 0)
        self.lab_dir = Label(text =self.initial_dir)
        self.lab_dir.grid(row = 0, column = 1)
        Label(text = "Source file:").grid(row = 1, column = 0)
        self.lab_source = Label(text =self.source_file)
        self.lab_source.grid(row = 1, column = 1)

        Label(text = "Destination audio file:").grid(row = 2, column = 0)
        Label(text = "Destination video file:").grid(row = 3, column = 0)
        self.lab_dest_audio = Label(text = self.dest_audio_file)
        self.lab_dest_audio.grid(row = 2, column = 1)
        self.lab_dest_video = Label(text = self.dest_video_file)
        self.lab_dest_video.grid(row = 3, column = 1)

        self.but_add_file = Button(text = 'Convert file', command = self.oggSplit)
        self.but_add_file.grid(row = 5, column = 3)

        #self.but_test = Button(text = "TEST", command = self.test)
        #self.but_test.grid(row = 10, column = 0)

    def test(self):
        pass


    def add_file(self):
        self.source_file = askopenfilename(initialdir = '/home/perwagner/Videos')
        head, tail = self.path_leaf(self.source_file)
        self.initial_dir = head
        self.source_filename = tail

        self.lab_source.config(text = self.source_filename)
        self.lab_dir.config(text = self.initial_dir)

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

        for file in files:
            filename=file
            file = self.initial_dir + "/" + file
            if "theora_" in file:
                os.rename(file, self.initial_dir + "/" + "video_" + self.source_filename + ".ogv")
            if "vorbis_" in file:
                os.rename(file, self.initial_dir + "/" + "audio_" + self.source_filename + ".oga")
            if "unknown_" in file:
                os.rename(file, self.initial_dir + "/" + "unknown_" + self.source_filename)




# Main program
root = Tk()
app = App(root)

root.mainloop()
