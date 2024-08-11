class AgoricSDK:
    def __init__(self):
        self.modules = {}

    def add_module(self, name, module):
        self.modules[name] = module

    def get_module(self, name):
        return self.modules.get(name, None)
