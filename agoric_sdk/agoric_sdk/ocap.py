class Capability:
    def __init__(self, name, access_function):
        self.name = name
        self.access_function = access_function

    def execute(self, *args, **kwargs):
        return self.access_function(*args, **kwargs)

class ObjectWithCapabilities:
    def __init__(self):
        self.capabilities = {}

    def add_capability(self, capability_name, access_function):
        capability = Capability(capability_name, access_function)
        self.capabilities[capability_name] = capability

    def get_capability(self, capability_name):
        return self.capabilities.get(capability_name)

class AccessControl:
    def __init__(self):
        self.objects_with_capabilities = {}

    def register_object(self, obj_name, obj):
        self.objects_with_capabilities[obj_name] = obj

    def grant_capability(self, obj_name, capability_name, *args, **kwargs):
        obj = self.objects_with_capabilities.get(obj_name)
        if obj:
            capability = obj.get_capability(capability_name)
            if capability:
                return capability.execute(*args, **kwargs)
            else:
                raise ValueError(f"No capability named {capability_name}")
        else:
            raise ValueError(f"No object named {obj_name}")

# Usage Example
def secret_function(data):
    return f"Secret data: {data}"

# Create an object with capabilities
secure_object = ObjectWithCapabilities()
secure_object.add_capability("access_secret", secret_function)

# Register the object with the access control system
access_control = AccessControl()
access_control.register_object("SecureObject", secure_object)

# Grant access to the capability
result = access_control.grant_capability("SecureObject", "access_secret", "Sensitive Info")
print(result)
