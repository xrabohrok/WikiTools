from Tkinter import Tk
import string
import os


class parseIntoWiki:
    def __init__(self):
        # create a TKinter window so I can rip the clipboard
        self.collection = []
        t = Tk()
        t.withdraw()
        self.clip = t.selection_get(selection="CLIPBOARD")

        # for when we have the clipboard figured out
        # r.clipboard_clear()
        # r.clipboard_append('i can has clipboardz?')

        t.destroy()

    def parseCommon(self, columnDelim):
        if len(self.clip) > 0:
            self.collection = string.split(self.clip, os.linesep)
            for i in self.collection:
                print(i)
        else:
            exit("NonConvertable Clipboard Contents")

    def parseCSVFromClip(self):
        return None

    def parseTSVFromClip(self):
        self.parseCommon("\t")
