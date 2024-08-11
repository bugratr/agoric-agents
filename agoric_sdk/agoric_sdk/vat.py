class Vat:
    def __init__(self, name):
        self.name = name
        self.resources = {}

    def add_resource(self, resource, quantity):
        if resource in self.resources:
            self.resources[resource] += quantity
        else:
            self.resources[resource] = quantity

    def get_resources(self):
        return self.resources
