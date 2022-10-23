def bold(func):
    def wrap():
        return f"<b>{func()[:-4]}<\\b>{func()[-4:]}"

    return wrap


def italic(func):
    def wrap():
        return f"<i>{func()}<\\i>"

    return wrap


@bold
@italic
def get_text():
    return "The quick brown fox jumps over the lazy dog"


print(get_text())
