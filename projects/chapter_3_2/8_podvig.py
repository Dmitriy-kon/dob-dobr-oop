from functools import wraps


class Handler:

    def __init__(self, methods="GET"):
        self.methods = methods

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    
    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"
    
    def __call__(self, *args, **kwargs):
        func, *other = args
        
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            m = request.get("method", "GET")
            if m in self.methods:
                m = m.lower()
                return self.__getattribute__(m)(func, request, *args, **kwargs)
        
        return wrapper