class Capability:
    def __init__(self, name):
        self.name = name
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def get_permissions(self):
        return self.permissions
