def bold(cls):
    class NewClsBold:
        def __init__(self):
            self.text = ""
            self.change_text()

        def change_text(self):
            cls_text = cls().init_text
            self.text = f"<b>{cls_text[:-4]}<\\b>{cls_text[-4:]}"

    return NewClsBold


def italic(cls):
    class NewClsItalic:
        def __init__(self):
            self.init_text = ""
            self.change_text()

        def change_text(self):
            self.init_text = f"<i>{cls().standard_text}<\\i>"

    return NewClsItalic


@bold
@italic
class Pen:
    def __init__(self):
        self.standard_text = "The quick brown fox jumps over the lazy dog"


tool = Pen()
print(tool.text)
