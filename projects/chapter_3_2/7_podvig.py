class HandlerGET:

    def __init__(self, func):
        self.func = func
        
    
    def get(self, func, request):
        return f"GET: {func(request)}"

    def __call__(self, request, *args, **kwargs):
        m = request.get("method", "GET")
        if m == "GET":
            return self.get(self.func, request)
        
        return None