class CustomException(Exception):
    def __init__(self, msg):
        with open("logs.txt", "a") as log_file:
            log_file.write(f'Error: {msg}\n')




raise CustomException("any error")
