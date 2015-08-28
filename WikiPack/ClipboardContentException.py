class ClipboardContentException():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("This value from the clipboard is not usable:" + self.value)
