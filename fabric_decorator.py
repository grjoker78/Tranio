def fabric_decorator(number):
    def fabric_d(function):
        def decorator(*args, **kwargs):
            try:
                r = function(*args, **kwargs) * number
                return r
            except BaseException:
                return 'None'
        return decorator
    return fabric_d