data = {}

class __init__:
    def __init__(self, name):
        data["name"] = name
        data["lay"] = None
        data["imports"] = None
        
        data["title"] = None
        data["favicon"] = None
        data["meta"] = None
        
    def layout(self, layout: dict):
        data["lay"] = layout
        
    def Import(self, imports: dict):
        data["imports"] = imports
        
    class style:
        def title(title: str):
            data["title"] = title
        
        def favicon(favicon: str):
            data["favicon"] = favicon
            
        def meta(meta: dict):
            data["meta"] = meta
        
def getData():
    return data