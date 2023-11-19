def func(text):
    def text_lower():
        return text.lower()
    return text_lower()

print(func('FFF'))