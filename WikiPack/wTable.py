from Tkinter import Tk


class parseIntoWiki:
    def __init__(self):
        # create a TKinter window so I can rip the clipboard
        t = Tk()
        t.withdraw()
        self.clip = t.selection_get(selection="CLIPBOARD")
        t.destroy()

    def parseCommon(self):
        print(self.clip)

    def parseCSVFromClip(self):
        return None

    def parseTSVFromClip(self):
        self.parseCommon()
