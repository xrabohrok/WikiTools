from unittest import TestCase
from wTable import parseIntoWiki
from Tkinter import Tk

from ClipboardContentException import ClipboardContentException


def setup_clipboard(stuff):
    t = Tk()
    t.withdraw()
    t.clipboard_clear()
    t.clipboard_append(stuff)
    t.destroy()


class TestParseIntoWiki(TestCase):
    def setUp(self):
        self.testObject = parseIntoWiki()

    def tearDown(self):
        self.testObject = None

    def test_getFromClipboard(self):
        self.fail()

    def test_parsecommon_detects_bad_clipboard(self):
        setup_clipboard("")
        blah = ""
        try:
            blah = self.testObject.parseCommon("\t")
        except ClipboardContentException as cce:
            print(str(cce))
            return
        contents = ""
        for i in blah:
            contents += i + "\n"
        self.fail("No/Unexpected exception thrown" + str(contents))

    def test_parseCommon(self):
        self.fail()

    def test_parseCommon2(self):
        self.fail()

    def test_parseCSVFromClip(self):
        self.fail()

    def test_parseTSVFromClip(self):
        self.fail()
