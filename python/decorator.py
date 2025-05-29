def param_dec(option):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # probably use option in here
            # before
            result = func(*args, **kwargs)
            # after
            return result

        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        return wrapper

    return decorator
