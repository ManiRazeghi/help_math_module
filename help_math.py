from functools import wraps

def check_type_input(data: list):
    def decore(func):
        @wraps(func)
        def inner(*args):
            for ind, inputer in enumerate(list(args)):
                if not isinstance(inputer, data[ind]):
                    raise TypeError(f'inputer "{inputer}" is not type as {data[ind]}')
            
            return func(*args)
        
        return inner
    
    return decore