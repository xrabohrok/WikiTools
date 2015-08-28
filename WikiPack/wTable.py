from Tkinter import Tk
import ClipboardContentException
import string
import os


# http://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python

class parseIntoWiki:
    def __init__(self):
        # create a TKinter window so I can rip the clipboard
        self.clip = []
        self.collection = []

    def getFromClipboard(self):
        t = Tk()
        t.withdraw()
        stuff = t.selection_get(selection="CLIPBOARD")
        # for when we have the clipboard figured out
        # r.clipboard_clear()
        # r.clipboard_append('i can has clipboardz?')

        t.destroy()
        return stuff

    def parseCommon(self, columnDelim):
        self.clip = self.getFromClipboard()
        if len(self.clip) > 1:
            self.collection = string.split(self.clip, os.linesep)
        else:
            raise ClipboardContentException("NonConvertable Clipboard Contents")
        return self.collection

    def parseCSVFromClip(self):
        return None

    def parseTSVFromClip(self):
        self.parseCommon("\t")
