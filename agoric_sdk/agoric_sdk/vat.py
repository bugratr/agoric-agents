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

    def execute_task(self, task_name, *args, **kwargs):
        if task_name in self.resources:
            print(f"Executing {task_name} with resources {self.resources[task_name]}")
            # Görev mantığı burada uygulanabilir
            result = f"Task {task_name} completed using resources."
            return result
        else:
            raise ValueError(f"No resources available for {task_name}")

# Usage Example
vat = Vat("ComputeVat")

# Kaynak ekleme
vat.add_resource("CPU", 10)
vat.add_resource("Memory", 32)
print("Current resources:", vat.get_resources())

# Görev çalıştırma
result = vat.execute_task("CPU", task_duration=5)
print(result)
