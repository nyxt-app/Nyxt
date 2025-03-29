data = {}

class Router:
    def __init__(self):
        data["routeStyle"] = None
        data["routes"] = None
        
    class style:
        def custom():
            data["routeStyle"] = "custom"
            
        def default():
            data["routeStyle"] = "default"
        
    def routes(self, routes: dict):
        data["routes"] = routes
        
    class Config:
        def __init__(self):
            data["config"] = {}
        
        def chunkPreloader(self, chunkPreloader: bool):
            data["config"]["chunkPreloader"] = chunkPreloader
        
        def NLinkElement(self, NLinkElement: bool):
            data["config"]["NLinkElement"] = NLinkElement
        
def getData():
    return data