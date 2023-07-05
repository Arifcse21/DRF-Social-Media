from django.http import HttpResponseBadRequest
from typing import Any


class JWTRequired:
    def __init__(self, view_func) -> None:
        self.view_func = view_func
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if not "Authorization" in request.headers:
            return HttpResponseBadRequest("Authorization headers missing!")
        
        return self.view_func(self, *args, **kwds)
    