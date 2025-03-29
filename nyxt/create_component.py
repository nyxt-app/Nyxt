data = {}

class __init__:
    def __init__(self, name: str):
        if not name in data:
            data[name] = {}
            data[name]["content"] = ""
            self.n = name
        else:
            raise Exception("Component name already exists")
        
    def content(self, htmlContent: str):
        data[self.n]["content"] = htmlContent
        
    def __repr__(self):
        return data[self.n]["content"]
        
def getData():
    return data