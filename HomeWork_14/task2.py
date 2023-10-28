def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for i in words:
                res = res.replace(i, '*')
            return res
        return wrapper
    return decorator



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))