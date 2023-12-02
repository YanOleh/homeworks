import logging
import os

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def count(self):
        try:
            self.file_len = open(self.filename, 'r')
            self.character_count = len(self.file_len.read())
            return self.character_count
        except FileNotFoundError:
            print("No such file or directory: 'example.txt'")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        logging.info(f"File '{self.filename}' opened. Character count: {self.count()}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


logging.basicConfig(level=logging.INFO)

with FileContextManager('example.txt', 'r+') as file:
    file.seek(0)
    print(f'Before: {file.read()}')
    file.write('Hello')
    file.seek(0)
    print(f'After: {file.read()}')
print(file.closed)















